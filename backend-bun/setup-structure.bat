@echo off

REM Creează directoare
mkdir agents
mkdir agents\mediaGenerator
mkdir services
mkdir utils
mkdir controllers
mkdir routes
mkdir database
mkdir database\models
mkdir config

REM Creează fișiere
type nul > agents\parserAgent.js
type nul > agents\conceptMapperAgent.js
type nul > agents\mediaGenerator\imageAgent.js
type nul > agents\mediaGenerator\voiceAgent.js
type nul > agents\courseBuilderAgent.js

type nul > services\geminiService.js
type nul > services\stableDiffusionService.js
type nul > services\coquiTTSService.js

type nul > utils\pdfParser.js
type nul > utils\wordParser.js
type nul > utils\structureUtils.js
type nul > utils\mindmapUtils.js

type nul > controllers\uploadController.js
type nul > controllers\parseController.js
type nul > controllers\generateController.js

type nul > routes\upload.js
type nul > routes\parse.js
type nul > routes\generate.js

type nul > database\models\User.js
type nul > database\models\Course.js
type nul > database\models\Media.js

type nul > config\default.json
type nul > README.md
