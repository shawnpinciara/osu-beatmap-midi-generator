import math
import random


song_title = "title";
song_artist = "title";
song_difficulty_name = "noobies";
song_tags = "tag1 tag2 tag3";
map_creator = "SongShuKuai"

difficulty_HPDrainRate = 5; #HP setting (0–10)
difficulty_CircleSize = 5; #CS setting (0–10)
difficulty_OverallDifficulty = 5; #OD setting (0–10)
difficulty_ApproachRate = 5; #AR setting (0–10)
difficulty_SliderMultiplier = 1.4; #Base slider velocity in hecto-osu! pixels per beat
difficulty_SliderTickRate = 1; #Amount of slider ticks per beat

events_backgroundImage = "bg.jpg";

beatmapId = (random.randint(0,1)*9000000) + 1000000;
beatmapSetID = (random.randint(0,1)*9000000) + 1000000;
song_name = "song.mp3"
beatmap_head = '''osu file format v14\n
                            [General]\n
                            AudioFilename: '''+song_name+'''\n
                            AudioLeadIn: 0\n
                            PreviewTime: -1\n
                            Countdown: 0\n
                            SampleSet: Soft\n
                            StackLeniency: 0.7\n
                            Mode: 0\n
                            LetterboxInBreaks: 0\n
                            WidescreenStoryboard: 0\n

                            [Metadata]\n
                            Title:'''+ song_title + '''\n
                            TitleUnicode:'''+ song_title + '''\n
                            Artist:'''+ song_artist + '''\n
                            ArtistUnicode:'''+ song_artist + '''\n
                            Creator:'''+ map_creator + '''\n
                            Version:'''+ song_difficulty_name + '''\n
                            Source: TV\n
                            Tags:'''+ song_tags + '''\n
                            BeatmapID:'''+ str(beatmapId) + '''\n
                            BeatmapSetID:'''+ str(beatmapSetID) + '''\n

                            [Difficulty]\n
                            HPDrainRate:'''+ str(difficulty_HPDrainRate)  + '''\n
                            CircleSize:'''+ str(difficulty_CircleSize) + '''\n
                            OverallDifficulty:'''+ str(difficulty_OverallDifficulty) + '''\n
                            ApproachRate:'''+ str(difficulty_ApproachRate) + '''\n
                            SliderMultiplier:'''+ str(difficulty_SliderMultiplier) + '''\n
                            SliderTickRate:'''+ str(difficulty_SliderTickRate) + '''\n

                            [TimingPoints] \n
                            ''';
                             
##Read midi

import mido

mid = mido.MidiFile('test2.MID', clip=True)
# mido.parse(mid)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        arr = str(msg).replace(' ','=').split('=')
        if arr[0]== 'note_on' or arr[0]== 'note_off':
            print(arr)
# for m in mid.tracks[0][0:]:
#     print(m)

##Generate hit objects and metadata