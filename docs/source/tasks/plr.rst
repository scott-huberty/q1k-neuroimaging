Gap Overlap (GO)
================

.. _GO-image:

.. figure:: https://raw.githubusercontent.com/scott-huberty/Q1K-doc-assets/main/_images/task_images/Q1K-Gap-Overlap.png
    :alt: Gap Overlap
    :align: center

    Gap-Overlap stimuli and interest area placement and sizing.


The Gap Overlap task measures reaction times from a central stimulus to a peripheral
stimulus. A central stimulus is first presented (spinning clock), followed by a
peripheral stimulus (Cloud), either ``803px`` eccentricity to the left or right. After
the participant gazes to the peripheral stimulus (or if the trial times-out), A reward
animation (star) is presented at the same place as the peripheral stimulus. Sounds are
played when the central and peripheral stimuli are presented. The color of the
background screen is randomly selected before the session begins, and reamins the same
for all trials.

.. vimeo:: 874134383
    :align: center

Conditions
----------

Baseline condition
    the central fixation disappears simultaneously with the
    presentation of the peripheral stimulus
Gap condition
    the central fixation disappears 200 ms before the presentation of
    the peripheral stimulus
Overlap condition
    the central fixation disappears 200 ms after the presentation of
    the peripheral stimulus

Interest Areas
--------------

The Central, Peripheral and Reward stimuli all have corresponding interest area (IA)
regions: Non-overlapping elliptical resources with a diameter of ``450px``,
shown as red circles in :numref:`GO-image`. This produces a ``108px`` buffer around the
stimulus. There is also a ``700*1080px`` IA that detects gaze to the wrong side of the
screen (shown in :numref:`GO-image`). This informs the trial classifier, as gaze to the
wrong side of the screen invalidates the trial.


Gaze Triggers
-------------

Gaze behaviors are classified by low-latency Invisible boundary (IB) gaze triggers,
that fire near immediately after gaze is detected within the IA. To begin a trial, the
participant’s gaze must stay within the ``450px`` diameter IA around the Central
stimulus for ``500ms``. The IB trigger for the 'wrong side' of the screen IA will fire
immediately if any gaze is allocated within that IA. Gaze must be within the Peripheral
Stimulus IA region for ``50ms`` to trigger this IB. This small delay in firing makes
sure that gaze is kept within the target IA before it is classified as such. 

.. note::
    The Saccadic RT from the central to peripheral stimuli is calculated using the
    *first* gaze sample within peripheral stimulus IA, not first gaze sample that
    meets the ``50ms`` threshold.

Classifiers
-----------
To aid the researchers running the study with real-time information, classifiers in the
experiment check for certain behaviors required for a valid trial. A trial is deemed
valid if: 

1. The saccade RT value is less than ``1200ms``.
2. The saccade RT is greater than the ``100ms``. 
3. There was is gaze to the wrong side of the screen. 

Valid trials are added to a count to the valid sum for that type of trial shown on the
Eyelink Host PC (``"Gap"``, ``"Overlap"``, and ``"Baseline"``).


Animations
----------
Central Stimulus
    At the onset of a trial the Central Stimulus is ``0*0px`` and over ``300ms``
    increases in size to ``350*350px`` (looming). Following this the Central
    Stimulus pulses, increasing/decreasing between ``234*234px`` to ``350*350px`` at
    3Hz (throbbing). Once gaze is detected, the Central Stimulus sized ``234*234px``
    spins clockwise at 1.5Hz.
Peripheral Stimulus
    Following the onset of the Peripheral Stimulus, gaze to it triggers a rotation
    animation. The Peripheral stimulus sized at ``234*234px`` rotates clockwise at
    1.5Hz. Finally,
Reward Stimulus
    the reward animation starts at ``234*234px``, reduces to ``0px`` as it rotates
    clockwise at 1.5Hz over 1 second (the reward duration).


