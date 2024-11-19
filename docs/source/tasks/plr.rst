.. _PR:

Pupillary light reflex (PLR)
============================

Overview
--------
The pupillary light reflex task measures the response of the pupil to intermittent flashes of light on a dark screen.
The task consists of 2 blocks of 32 trials each. In each trial, the fixation is presented for ``6`` seconds on a black 
background. After ``6`` seconds, the screen flashes white for ``75``ms. The participant must gaze at the fixation cross
to trigger the trial.

The table below shows event codes for EGI Net-Station acquisition, and DIN events triggered by the photo-diode on the
screen for each event.  
------------------------  --------
    Condition                
========================  ========     
``Flash``                   plro
 ``Beginning of trial``     VBeg
                            TSYN
                            DIN2
                            DIN3
                            DIN4 
========================  ======== 
