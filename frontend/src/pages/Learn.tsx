import { useState } from 'react';
import { motion } from 'framer-motion';
import { Upload, FileText } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";
import { Button } from '@/components/ui/button';
import Header from '@/components/Header';  // ✅ Import Header
import Footer from '@/components/Footer';  // ✅ Import Footer

const Learn = () => {
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const { toast } = useToast();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
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
    formData.append("pdf", file);

    try {
      const response = await fetch("http://localhost:3000/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Upload failed");
      }

      const data = await response.json();
      console.log("Upload success:", data);

      if (data.videoUrl) {
        const videoPath = `http://localhost:3000${data.videoUrl}`;
        console.log("Video Path:", videoPath);
        setVideoUrl(videoPath);
      } else {
        throw new Error("No video URL returned");
      }

      toast({
        title: "Success!",
        description: "Your file has been processed successfully",
      });

    } catch (error) {
      console.error("Upload error:", error);
      toast({
        title: "Upload failed",
        description: error.message,
        variant: "destructive",
      });
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header />  {/* ✅ Header adăugat */}

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
                Upload your PDF and generate a video visualization using AI.
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
                  The AI will generate a video visualization of key concepts.
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

                <Button 
                  onClick={handleUpload} 
                  disabled={!file || isUploading}
                  className="bg-primary text-white hover:bg-primary/90"
                >
                  {isUploading ? "Processing..." : "Process Document"}
                </Button>
              </motion.div>

              {videoUrl && (
                <div className="mt-6 text-center">
                  <h2 className="text-xl font-bold mb-2">Generated Video</h2>
                  <video controls width="640">
                    <source src={videoUrl} type="video/mp4" />
                    Your browser does not support the video tag.
                  </video>
                </div>
              )}
            </div>
          </div>
        </section>
      </main>

      <Footer />  {/* ✅ Footer adăugat */}
    </div>
  );
};

export default Learn;
