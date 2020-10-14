
# python crop-video.py --inp ./data_test_02/dona.mp4
# Result: ffmpeg -i ./data_test_02/dona.mp4 -ss 0.0 -t 9.80980980980981 -filter:v "crop=480:492:0:166, scale=256:256" crop.mp4
# Exec result: ffmpeg -i ./data_test_02/dona.mp4 -ss 0.0 -t 9.80980980980981 -filter:v "crop=480:492:0:166, scale=256:256" crop.mp4
# python demo.py  --config config/vox-adv-256.yaml --driving_video crop.mp4 --source_image data_test_02/kim.jpeg --checkpoint checkpoints/vox-adv-cpk.pth.tar --relative --adapt_scale


# ffmpeg -i crop.mp4 -i result.mp4 -filter_complex hstack finished_video.mp4

import ffmpeg

input_video = ffmpeg.input('guy_parmelin/result.mp4')

input_audio = ffmpeg.input('guy_parmelin/crop.mp4')


ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()