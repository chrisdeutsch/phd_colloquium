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
    electron or muon, and a hadronic tau decay
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

- 
