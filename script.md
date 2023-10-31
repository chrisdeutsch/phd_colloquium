# Colloquium Script

## The Standard Model (Sl. 1)

- SM -- Our current best model for particles and their interaction
- Rel. quantum field theory: Dynamics of fields described by a Lagrangian
  density
- Electromagnetic, Strong, Weak (3 out of 4) described by symmetry principle
  (local gauge invariance)
  - Local gauge transformations leave the Lagrangian unchanged
  - Problem: Particles cannot have masses, otherwise this would not hold!
- Solution from the 60s: Dynamical mass generation through symmetry breaking
  - Introduce a new scalar field phi (coupling to fermions & gauge bosons)
  - Key player the Higgs potential which causes Spontaneous Symmetry Breaking
    and is a central element of this thesis


## Electroweak Symmetry Breaking (Sl. 2)

- This is a toy model of what this potential looks like
- Field zero -> symmetric state but unstable
  - Imagine a ball -- a tiny perturbation would roll it down the hill
- Lowest energy state (vacuum state): appears to break the symmetry
  - Value of the field in the vacuum state -> vacuum expectation value
- Cannot solve the Lagrangian directly: Have to use perturbation theory (about minimum)
  - Gives rise to masses for Gauge bosons
  - Moreover, the Yukawa couplings of Fermions to the Higgs field provides
    fermion masses proportional to the Yukawa coupling strength


## Higgs Discovery (Sl. 3)

- While this seems fairly abstract, the Higgs boson was discovered in 2012 by
  the ATLAS and CMS collaborations at the LHC
- In the H->yy channel and H -> ZZ -> 4 lepton channel
- Mass of about 125 GeV
- Nobel prize awarded the following year


## 11 Years of Higgs Boson Measurements (Sl. 4)

- We have come a long way since the discovery
- Higgs boson mass is known to per mille level
- Gauge boson and Yukawa couplings are in excellent agreement with the SM
  prediction
  - Many couplings observed and measured with ca. 10% precision
  - The line shows the mass-dependent coupling strength
  

## The Higgs Boson Self-Coupling (Sl. 5)

- This is the Higgs potential expanded about the vacuum state
- With the discovery of the Higgs boson, we have a direct experimental
  measurement of the first term, which determines the mass of the Higgs boson.
- In the SM, the remaining terms are thus fully determined. However, we have
  never explicitly measured them.
  - These terms describe couplings between three or four Higgs bosons (Higgs
    boson self-coupling)


Overlay:
- Deformations of the Higgs potential yielding the same Higgs mass but different
  higher-order terms
- Only possible in BSM theories!
- We probe this experimentally by measuring Pair Production of Higgs Bosons!


## Higgs Boson Pair Production in the SM (Sl. 6)

- Two most relevant production processes in pp collisions at 13 TeV
- Gluon gluon fusion:
  - Two Feynman diagrams
  - Box -- Top box not involving the self coupling
  - Triangle -- Involving the trilinear self-coupling
  - Fairly low cross section: Destructive interference
- Subdominant contribution: VBF
  - Three diagrams: one involving the self-coupling, the others Higgs-Vector
    couplings
  - Even lower cross section: We don't target this explicitly

- The SM cross sections are too small to detect these processes. A thousand
  times smaller than single Higgs boson production!


## Beyond the Standard Model (Sl. 7)

- While the SM is tested in many areas to great precision
- We know the SM is incomplete. For example:
  - We have no explanation for the lack of Antimatter in the universe
  - We do not attempt to describe Gravitation at all
  - We only know about 5% of the energy content of the universe. The rest is
    dark matter (25%) which is matter that we can only see indirectly through
    its gravitational interaction. And dark energy (65%) which causes the
    accelerating expansion of the universe, which is even more ominous.
- To explain these, we need to go beyond the SM

- Some theories, such as theories with extended Higgs sectors, predict new
  scalars X. If these are sufficiently massive, they can decay into two SM-like
  Higgs bosons. This is something we can also look for when searching for Higgs
  boson pair production.
- This we do, considering mX from 251 GeV to 1.6 TeV


## The ATLAS Experiment at the LHC (Sl. 8)

- Coming to the experimental aspects of my thesis
- We used the Large Hadron Collider in Geneva to accelate protons to an energy
  of 6.5 TeV yielding a CM energy of 13 TeV
- Protons collide at multiple interaction points at which different experiments
  are located

- At one of them is the ATLAS experiment which I worked at
- The detector covers the interaction point 
  - Inner detector for tracking of charged particles
  - Calorimeters for energy measurement of most charged and neutral hadrons
  - Muon system to track muons that are able to traverse the detector
- Combining these detector technologies, we can perform almost a full event
  interpretation from the measured signals


## Final States of Searches for HH Production (Sl. 9)

- When searching for Higgs boson pair production, a diverse set of final states
  can be considered
- Table shows the branching ratios of a di-Higgs system
- Currently, the most promising channels are bbbb, bbtautau, bbyy
  - These achieve a suitable trade-off between branching ratio & cleanliness of
    final state. Cleanliness being the ability to select events of interest and
    reject background processes.


## The bbtautau final state (Sl. 10)

- In my thesis, I consider the bbtautau final state
  - Combines the large branching ratio of H->bb with the distinct signature of
    H->tautau (to efficiently select events and reject backgrounds)
- We break down the bbtautau final state into two channels
  - lephad: 2 b-jets (can be identified by displaced decays of b hadrons), one
    electron or muon (from a leptonic tau decay), and a hadronic tau decay
  - hadhad: Instead of the electron muon -> another hadronic tau decay. I
    largely focused on this final state.
  - This covers the largest share of di-tau system decays.
  
- An important part of the bbtautau channel is the ability to identify hadronic
  tau lepton decays. Even moreso in hadhad. -> Interlude
  
## Tau Identification (Sl. 11)

- Tau identification is the process of distinguishing actual hadronic tau lepton
  decays from other signatures in the detector
- Particularly important are quark- or gluon-initiated jets which are reasonably
  similar. But there are some differences!
  - Go over differences

- This is a classification problem: use machine learning to distinguish the two cases


## Tau Identification: Input Variables (Sl. 12)

- We need to use numeric variables to distinguish the two cases
- First, we can consider "high-level variables": That is variables that we
  construct ourselves to be sensitive to the differences
  
- Before I started my work in ATLAS, this is the only information we used to
  perform Tau-ID. We used these variables in "Gradient Boosted Trees".
- However, in doing so we might lose some information that could help in the classification

- Idea: include also low-level information. That is, information about particle
  trajectories reconstructed with the ID and topological clusters of energy in
  the calorimeters.
- We consider tracks close to a reconstructed tau candidate. But we cap it at 10
  - For each track we provide track-specific variables such as track pT, angular
    distances, impact parameters, etc.
- Similarly, we consider up to 6 clusters associated with the tauhad seed jet
  - ET, angular distances, and cluster moments which describe the shape of a
    cluster

- One difference: the number of tracks and clusters is variable. This does not
  fit that nicely into a gradient boosted tree approch.


## Tau Identification: Network Architecture (Sl. 13)

- A more natural machine learning method for this problem are recurrent neural
  networks
- Recurrent neural networks are designed to work with variable-length input
  sequences, such as the tracks and clusters we want to consider for Tau-ID
- The chosen architecture has three branches. One for each input type:
  - High-level variables: Just a regular densely connected neural network
  - Track & Cluster branches: Recurrent neural network based that summarises the
    variable sequence to a fixed output
- Everything is merged and reduced to a single output number
- This number, after training, corresponds to the conditional probability of a
  given candidate being a tauhad or a q/g jet given the input features.


## Tau Identification: Performance (Sl. 14)

- How well this works is shown in this plot. Here I show:
  - Selection efficiencies for true hadronic tau decays (true positive rate)
  - Rejection factor for quark/gluon-initiated jets (1 / false positive rate)
  - Red lines: 1-prong taus
  - Blue lines: 3-prong taus
  - Dashed: Previous BDT-based method
  - Solid: The recurrent neural network approach

- Dramatic improvement: 80% for 1-prong, 40-80% for 3-prong tau candidates


## Interlude End

- Now moving back to the experimental aspects of the Higgs pair production
  search
- Beginning with what detector signatures we consider to be b-jets, hadronic tau
  decays, etc.


## Object Selection (Sl. 15)

- We used a very basic definition of most physics objects
- ...


## Event Selection (Sl. 16)

- After having defined the physics objects, we can apply a rough selection to
  reduce the data to the events of interest
- We split into three channels based on the trigger that selected the event:
  - hadhad channel, lephad SLT, lephad LTT


## Signal Acceptance (Sl. 17)

- How likely are we to select an event of interest produced in a pp collision?
  - Event of interest is here either bb tauhad tauhad or bb tauhad taulep
- Table shows the SM HH case and compares it to the previous analysis performed
  in this channel
  - We see a very large improvement in acceptance compared to the previous round
- The figure shows the acceptance for a BSM signal from resonant HH production 
  - At low mass, we are limited by the trigger thresholds
  - At high mass, the reconstruction fails because the Higgs decay products
    start to be too close due to the Lorentz boost


## Background Estimation (Sl. 18)

- We have various background processes that contribute significantly after our
  event selection
- These have to be estimated! We use different techniques to do so.
  - Go over table
- In the following I will focus mostly on the hadhad channel.
  - To get an idea how large the backgrounds are, the fractions are listed here
  
I will now go over some of the background estimation techniques we use:


## Z+jets (Sl. 19)

- ...


## ttbar with fake tauhadvis (Sl. 20)

- We are generally not sure, how well MC simulation models the background
  contributions that include q/g jets misidentified as hadronic tau decays
- ...

TODO: Add a SF plot?


## Background Estimation: Multi-Jet (Sl. 21)

- ...


## Signal Sensitivity After Event Selection

- After the backgrounds are estimated, we can have a look at the expected event
  yields in the different channels.
- As you can see, we only expect a handfull of SM HH events in all three channels
- However, we expect a very large number of background events ranging from 6k to
  100k.
- Clearly, when doing a statistical analysis of the counts, there is no relevant
  sensitivity to the signal.
- However, we can use event properties to further narrow in on our signal.


## Discriminating Variables

- Here are some examples of event properties in the hadhad channel that help us
  to do that.
- Can use the reconstructe di-tau system mass: Should peak at 125 GeV for the
  signal. The background has a broad distribution.
- Similarly, for the di-b system mass.
- The final example is the angular distance between the two taus. Generally, for
  SM HH and resonances with high mass, we expect the Higgs bosons to be produced
  with high pT. As a result of the Lorentz boost, the decay products tend to be
  closely aligned.
  
- Ideally we want to use all of these properties as well as their
  interdependencies. Therefore, we use machine learning to exploit this
  information.
  

## Signal Extraction

- Specifically, for SM HH production we use simple binary classifiers. Namely,
  BDTs in the hadhad channel and NNs in the lephad channel.
- We can then use the predicted scores of the classifiers directly to perform a
  statistical analysis to look for our signal process.
- This is shown in the figure on the right, where you can see the binned score
  and how it nicely separates the signal from the background.
  

## Signal Extraction: Resonant HH Production

- We do something slightly different when looking for resonant production.
- The difference here is that we have multiple signal hypotheses. Namely, 20
  different assumed masses of X ranging from 251 GeV to 1.6 TeV
- The key point here is that the kinematic properties of signal events change
  with mX as you can see for example in the sketch on the bottom.

- Previously, we handled this by using many different BDTs trained for specific
  masses.

- Now our approach is different, however. We use what are called parameterised
  neural networks. These can be used to learn the continuous classification
  problem.
- These don't just make it simpler because only one classifier is needed. But
  also they tend to perform slightly better since you can solve the more general
  problem more efficiently. And you can also interpolate to parameter values
  that you don't have training events for.
  

## Statistical Analysis

- Using the BDT and Neural Network outputs, the statistical analysis is
  relatively straightforward.

- For SM HH we model the BDT, NN and mll distribution and fit them to observed data.
- For resonant HH production, we do the same for every mass point, however,
  using now the PNN evaluated at the given mass


## Discriminants After the Background-Only Fit

- Now moving to the results of the search for SM HH production.
- Here you can see the binned discriminants in the three SRs: the BDT in hadhad,
  and the two NNs in lephad. This is after fitting the b-only statistical model
  to data.
- You can see that the b-only model describes the data fairly well. You can
  formalize this and perform a statistical test of b-only vs signal+bkg. which
  yields a p-value of 27%.


## Upper Limits on the SM HH Signal Strength

- Given that we do not see any significant excess, we set an upper limit on the
  SM HH production cross section at 95% CL
- We set the upper limit at 4.7 times the SM cross section
- The expected upper limit under the b-only hypothesis is 3.9

- You can compare this to the bbbb and bbyy channels:
  - The three most promising channels set limits in a similar ballpark
  - bbyy sets the tightest limit, bbtautau is expected to be the most sensitive
  - We also combined the three searches... much better than we expected a few years ago

- Compare with our main competitor CMS
  - Best expected limit: bbbb (4.0)

- ATLAS bbtautau is the most sensitive channel to date!


## Search for Resonant HH Production: Discovery Tests

- We can do the same analysis also using resonant HH production as a signal hypothesis.
  - We only have to exchange the discriminants
- What we found there is an excess for scalars with mX = 1000 GeV
  - This excess is particularly located in the hadhad channel. Last bin
- Evaluated the statistical significance
  - 3.1 sigma local
  - 2.0 sigma global (taking into account the fact that we test multiple hypotheses)
  - NOT SIGNIFICANT BY CONVENTIONAL STANDARDS
  

## Search for Resonant HH Production: Upper Limits

- We can set upper limits on the resonant HH production cross section
- In bbtautau we set upper limits ranging from 1000 fb to about 20 fb depending
  on mass
- On the right you can see a similar plot, where the bbtautau channel is
  compared to bbyy and bbbb
  - There you can clearly see that the three channels are complimentary: at low
    mass bbyy, intermediate mass bbtautau, high mass bbbb


## Constraining the Higgs Boson Self-Coupling

- 
