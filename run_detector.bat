@echo off

echo ========================================= >> E:\securewatch-ai\detector_log.txt
echo Started %date% %time% >> E:\securewatch-ai\detector_log.txt

cd /d E:\securewatch-ai

call faceenv\Scripts\activate.bat >> E:\securewatch-ai\detector_log.txt 2>&1

python -m detection.failed_login_detector >> E:\securewatch-ai\detector_log.txt 2>&1