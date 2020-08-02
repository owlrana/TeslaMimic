# TeslaMimic
An open-source model that mimics the way Tesla can drive. Currently I am developing this independently, any kind of contribution is welcomed!

The idea behind this is to identify the markings on the road and train the model to identify the lane.
I tried removing unecessary marking points in a video through Adobe After Effects' scripts (I am comfortable with video editing) but it turns out their model does not exactly 
work the way I thought it would. So the videos taken are through dash-board cams which are raw footage available at https://research.google.com/youtube8m/ (can also find it in my repository) and I narrowed the search down to dashcam footages. Now there is a possibility that the videos MAY be a clickbait or include an accident. I don't think I have a way to find out if it IS a click-bait or not but guessing that the probability of a dashcam footage to be a clickbait would be fairly low (Dashcam footage, not including accidents is NOT a trending topic as of date xD) I have just removed the videos marked as accidents in the subset of dashcam. You can have any other approach, I am just going to update with the source code and maybe the final result (if I am succesfull, of course). 

So that's it, there are no rules as of how you can contruibute. Just make a pull request or contact me if you think you have something!

PS: I use colab.research.google.com and cloud.google.com to run my tests, so if there are any incompatibilites on PCs let me know I would like to fix them as well!

Let's do it
