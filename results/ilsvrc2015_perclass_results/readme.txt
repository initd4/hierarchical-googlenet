====================================================================
ImageNet Large Scale Visual Recognition Challenge 2015 (ILSVRC2015)
http://image-net.org/challenges/LSVRC/2015

Per-class results of participating teams
====================================================================

The folder contains 8 files:

(1) teamnames.txt
    Every row corresponds to one team
    Every listed team submitted 1 or more entries to participate in ILSVRC2015
    Every row is of the form
    	<teamid> <teamname>

(2-5) det_results.txt, loc_results.txt, cls_results.txt, vid_results.txt
    Every row corresponds to one submitted entry
    Every row is of the form
        <teamid> <submissionid> <bExternal> <result for class 1> ... <result for class N>
    teamid is as above in teamnames.txt
    submissionid is simply to distinguish different submissions within each team
    bExternal is 1 or 0 to indicate if the team used external training data
    N is the number of classes, 200 for detection (det_results.txt), 30 for detection
    from video (vid_results.txt), 1000 otherwise
    the result is AP for detection, localization/classification error otherwise

(6-8) meta_clsloc.mat and meta_det.mat and meta_vid.mat
    These files are also provided with the development kit for the challenge
    Loading them into matlab, you'll see a struct 'synsets'
    The synsets 1-200 in meta_det.mat correspond to the 200 detection classes
    The synsets 1-1000 in meta_clsloc.mat correspond to the 1000 localization/classification classes
    The synsets 1-30 in meta_vid.mat correspond to the 30 detection classes from video
    For more details please download the development kit for ILSVRC2015 and consult the readme

Please contact ilsvrc@image-net.org with any questions
