import sys
import os
import json
import librosa
import numpy

data = json.load(open(sys.argv[1], 'r'))
#os.remove(sys.argv[1])

if 'sampler' in data and 'stft' in data and 'persistance' in data:
	file = data['sampler']['file']
	del data['sampler']['file']

	y, sr = librosa.load(file, **data['sampler'])

	stft = abs(librosa.stft(y, **data['stft']))

	features = []
	if 'chroma' in data:
		features.append(librosa.feature.chroma_stft(S=stft, **data['chroma']).T)
	if 'mfcc' in data:
		features.append(librosa.feature.mfcc(S=stft, **data['mfcc']).T)
	if 'mel' in data:
		features.append(librosa.feature.melspectrogram(S=stft, **data['mel']).T)
	if 'rmse' in data:
		features.append(librosa.feature.rmse(S=stft, **data['rmse']).T)

	features = numpy.hstack(features)

	try:
		old_features = numpy.load(data['persistance']['save'])
		features = numpy.vstack([old_features, features])
	except:
		pass

	numpy.save(data['persistance']['save'], features)