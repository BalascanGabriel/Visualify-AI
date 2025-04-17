import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Upload, FileText, RefreshCw } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";
import { Button } from '@/components/ui/button';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import Mindmap from '@/components/Mindmap';

const Learn = () => {
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [mindmapData, setMindmapData] = useState<null | {
    nodesData: any[];
    linksData: any[];
  }>(null);
  const { toast } = useToast();

  // 🔄 Load from localStorage on mount
  useEffect(() => {
    const stored = localStorage.getItem("mindmap");
    if (stored) {
      const parsed = JSON.parse(stored);
      if (parsed?.nodesData && parsed?.linksData) {
        setMindmapData(parsed);
      }
    }
  }, []);

  // 💾 Save mindmap to localStorage on change
  useEffect(() => {
    if (mindmapData) {
      localStorage.setItem("mindmap", JSON.stringify(mindmapData));
    } else {
      localStorage.removeItem("mindmap");
    }
  }, [mindmapData]);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      toast({
        title: "Error",
        description: "Please select a file to upload",
        variant: "destructive",
      });
      return;
    }

    setIsUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:3001/api/generate", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      const data = await res.json();

      if (data?.mindmap) {
        setMindmapData({
          nodesData: data.mindmap.nodes,
          linksData: data.mindmap.links,
        });

        toast({
          title: "Succes!",
          description: "Mindmap generat cu succes.",
        });
      } else {
        throw new Error("Mindmap lipsă în răspuns.");
      }
    } catch (err: any) {
      toast({
        title: "Eroare",
        description: err.message,
        variant: "destructive",
      });
    } finally {
      setIsUploading(false);
    }
  };

  const handleReset = async () => {
    const confirmReset = window.confirm("Sigur vrei să ștergi tot?");
    if (!confirmReset) return;

    try {
      await fetch("http://localhost:3001/api/render/reset", { method: "POST" });
    } catch (err) {
      // ignorăm error la reset backend
    }

    setMindmapData(null);
    setFile(null);
    setVideoUrl(null);
    toast({
      title: "Reset complet",
      description: "Datele au fost șterse.",
    });
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header />

      <main className="flex-grow pt-20">
        <section className="py-16 bg-gradient-to-b from-secondary/30 to-transparent">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="max-w-3xl mx-auto text-center"
            >
              <h1 className="text-4xl md:text-5xl font-bold mb-6">Upload and Learn</h1>
              <p className="text-lg text-muted-foreground mb-8">
                Upload your PDF and generate a smart mindmap with AI.
              </p>
            </motion.div>
          </div>
        </section>

        <section className="py-12">
          <div className="container mx-auto px-4 md:px-6">
            <div className="max-w-3xl mx-auto">
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="p-8 border-2 border-dashed border-primary/30 rounded-xl text-center"
              >
                <FileText className="w-12 h-12 text-primary/60 mx-auto mb-6" />
                <h2 className="text-2xl font-bold mb-4">Upload Your PDF</h2>
                <p className="text-muted-foreground mb-6">
                  AI will analyze your content and generate a visual learning map.
                </p>

                <div className="mb-6">
                  <input
                    type="file"
                    id="file-upload"
                    className="hidden"
                    accept=".pdf"
                    onChange={handleFileChange}
                  />
                  <label
                    htmlFor="file-upload"
                    className="inline-flex items-center gap-2 px-4 py-2 bg-secondary rounded-md cursor-pointer hover:bg-secondary/80 transition-colors"
                  >
                    <Upload className="w-4 h-4" />
                    Choose File
                  </label>
                  {file && <p className="mt-2 text-sm font-medium">{file.name}</p>}
                </div>

                <div className="flex justify-center gap-4">
                  <Button
                    onClick={handleUpload}
                    disabled={!file || isUploading}
                    className="bg-primary text-white hover:bg-primary/90"
                  >
                    {isUploading ? "Processing..." : "Process Document"}
                  </Button>

                  {mindmapData && (
                    <Button onClick={handleReset} variant="destructive">
                      <RefreshCw className="w-4 h-4 mr-2" /> Reset
                    </Button>
                  )}
                </div>
              </motion.div>

              {mindmapData && (
                <div className="mt-10">
                  <h2 className="text-2xl font-bold text-center mb-4">Mindmap Generat</h2>
                  <div className="min-h-[950px] w-full border rounded-lg shadow-lg overflow-hidden">
                    <Mindmap
                      nodesData={mindmapData.nodesData}
                      linksData={mindmapData.linksData}
                    />
                  </div>
                </div>
              )}
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
};

export default Learn;
