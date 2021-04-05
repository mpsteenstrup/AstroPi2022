# program som detekterer biler mm

Progrmmet kan findes her,  [https://github.com/ecd1012/rpi_road_object_detection](https://github.com/ecd1012/rpi_road_object_detection)


```
# rename files
i=0; for f in *.jpg; do mv "$f" "$i.jpg";((i++));done

# video
ffmpeg -i %d.jpg -vcodec mpeg4 test.mp4

#Change directories to where you cloned the repo
cd ~/selfdriving/rpi_road_object_detection
python3 detection.py --modeldir=TFLite_model_bbd --output_path="/home/pi/selfdriving/rpi_road_object_detection/video"
```
