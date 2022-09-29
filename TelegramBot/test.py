from progress.bar import Bar
import time as time
import emoji as emoji

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.3)
    bar.next()
bar.finish()

print(emoji.emojize(':thumbs_up:'))