---
title: "Deep learning of tissue fate features in acute ischemic stroke"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2015
date: "2015-11-01"
venue: "BIBM 2015 Workshop on Biomedical Visual Search and Deep Learning, 2015"
authors: "Noah Stier, Nicholas Vincent, David Liebeskind, Fabien Scalzo"
source_url: "https://ieeexplore.ieee.org/document/7359869/"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W2220129321; CV ref [W2]; Full text from PubMed Central JATS XML (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5597003/)."
---

# Deep learning of tissue fate features in acute ischemic stroke

## Full text

I. Introduction

Recent clinical trials in acute ischemic stroke [2] have illustrated the possible benefits of endovascular clot-retrieval interventions, which have been shown to be efficient overall on a randomly sampled population. However, stroke is heterogeneous, and it is important to be aware of the balance of risk versus possible benefit of invasive treatment under the specific conditions of each patient. Methods are under ongoing development for analyzing this balance in different patient sub-groups. Given the state of the field, accurate data-driven models for assessing tissue damage could play a major role in the development of decision support systems for stroke clinicians. Deep learning algorithms show potential in this area, as they have been able to capture complex imaging features in the context of big data while remaining robust to significant levels of noise.

Within the last 30 years, brain imaging has revolutionized our understanding of stroke pathophysiology and paved the way for effective treatments. During an acute ischemic stroke, an area of the brain is deprived of blood circulation due to a clot in the supplying artery. Current treatments aim at maximizing the recovery of injured brain tissue by restoring blood flow in the affected artery. There is a recognized need for accurate clinical decision tools to identify, as early as possible, stroke patients with still-salvageable brain tissue who could benefit from such a treatment.

Infarct growth in ischemic stroke is a complex process that varies greatly across patients and remains poorly understood. Several factors (such as degree of reperfusion, quality of collateral flow, and age) have been shown to influence lesion growth [15], but their exact relationship over time remains to be clarified. In current clinical practice, the spatial mismatch [12], [6], [26], [5] between diffusion (DWI) and perfusion-weighted (PWI) magnetic resonance imaging (MRI) is often used to differentiate irreversible infarction from salvageable tissue. However, the DWI-PWI mismatch as a diagnostic parameter is not perfect, as tissue damage detectable using DWI may still be reversible. In addition, hypoperfusion is often analyzed using a simple threshold on a time-to-maximum-perfusion (Tmax) image, which is commonly derived from PWI [7]. A more sophisticated approach to Tmax analysis warrants investigation.

Predictive models of tissue fate based on computer vision and pattern recognition techniques may provide a more reliable and objective insight. Early models have been trained on a voxel-by-voxel basis using multimodal perfusion imaging. Among the techniques that have been studied are generalized linear model (GLM) [30], [31], Gaussian models [22] trained on multiple parameters (DWI, CBF, CBV, mean transit time (MTT)), logistic regression [32], and ISODATA clustering [28].

More recently, regional models of tissue fate that incorporate data in the area surrounding the target location have been shown to improve the accuracy of the predictive model, relative to single-voxel-based methods. These approaches exploit spatial correlation between voxels [18], a prior map of spatial frequency-of-infarct [27], Artificial Neural Networks [10], and spatio-temporal maps [21]. These methods have all demonstrated improvement over single-voxel-based approaches. Regional models based on spectral regression showed promising results in our previous studies [25], [24], [23] using different PWI parameters acquired from acute stroke patients: Tmax, MTT, and time-to-peak (TTP).

In the last two decades, the explosion of digital images and the availability of data storage and computational power have enabled researchers in many areas to approach big data from new perspectives. Deep learning has emerged as a highly versatile set of techniques and has been applied to various problems, such as handwritten character recognition [9], face detection and recognition [29], speech recognition [8], and image classification [13]. Machine learning algorithms, and Deep learning in particular, will likely revolutionize medical care as we know it, driving significant progress toward precise and individualized medicine. The near future will see machine learning algorithms provide decision support comparably to experts in the field of medical image analysis and radiology, providing valuable inputs to physicians via computer-aided diagnosis, image segmentation, image annotation and retrieval, image registration, and multimodal image analysis. So far, however, deep learning is primarily used as a research tool, and it has not yet been successfully translated to clinical practice.

In this paper, we follow these findings and trends to introduce a regional predictive model of tissue fate based on deep learning. The model uses tissue information available at symptom onset, specifically the Tmax parameter of PWI, to predict the tissue outcome at the time of the follow-up MRI (usually four days after intervention). Fluid-attenuated inversion recovery (FLAIR) images from patients' follow-up MRIs are used to determine which tissue survives, providing the ground truth for training the model, as FLAIR is regarded as the current gold standard in neurology to discern irreversible lesions [4].

II. MethodsA. Data Acquisition

The imaging data was collected from acute ischemic stroke patients admitted at the University of California, Los Angeles Medical Center. The use of these data was approved by the local Institutional Review Board (IRB) and introduced in our previous study [23]. Inclusion criteria for this study included: (1) Diagnosis of acute stroke, (2) last known well time within six hours, (3) Perfusion MRI of the brain performed before recanalization therapy and approximately four days later. A total of 25 patients (mean age, 56 ± 21 years; age range, 27 to 89; 15 women; average NIHSS of 14±6.3) satisfied the above criteria and underwent MRI using a 1.5 Tesla echo planar MR imaging scanner (Siemens Medical Systems). The PWI scanning was performed with a timed contrast-bolus passage technique (0.1 mg/kg contrast administered intravenously at a rate of 5cm3/s) and with the following parameters: repetition time (TR), 2000 ms (21 cases), 1920 ms (2), 1770 ms (1), 2890 ms (1); with an average echo time (TE) 44 ± 10.4 ms. The FLAIR sequence was acquired with the following parameters: repetition time (TR), 10000 ms (19 cases), 8800 ms (4), 8160 ms (1), 7000 ms (1); echo time (TE), 105 ms (20), 89 ms (3), 123 ms (1), 82 ms (1); inversion time (TI), 2400 ms (20), 2500 ms (4), 2472 ms (1), respectively. All the images were resized using bilinear interpolation to match a resolution of 1 × 1 × 5 mm per voxel. Average lesion size at onset is 10.35 ± 13.1cm3 and 43.6 ± 18.2cm3 at follow-up (as measured in FLAIR images at day 4). All patients had the revascularization success determined using the Thrombolysis in Cerebral Infarction (TICI) scale: TICI Score 3, 2b, and 2a in 5, 7, and 13 patients, respectively.

The FLAIR images taken approximately four days after symptom onset will be referred to as the follow-up images, and the PWI images taken during the presentation of acute symptoms will be referred to as the acute images.

B. Data Preprocessing1) Slice Extraction

The slice thickness of the perfusion MRI scans included in this study was between 5 and 7 mm and therefore would not provide enough granularity to model the relationship between slices. We therefore visually identify the transverse plane exhibiting the greatest lesion size in the acute data for each patient. We then extract that plane as a two-dimensional slice from the acute and from the follow-up images, to be used in the study.

2) Brain Volume Segmentation

This step was performed because non-brain tissue in the images can interfere with the image registration step, which was performed subsequently. The FSL Brain Extraction Tool (BET) was used to remove skull and non-brain tissue. BET estimates an intensity threshold to discriminate between brain/non-brain voxels. Then, it determines the center of gravity of the head, defines a sphere based on the center of gravity of the volume, and finally deforms it toward the brain surface.

3) Image Registration

It was necessary to register acute and follow-up images in order to match the tissue fate labels to their proper anatomical locations. Co-registration was performed for each patient independently. Because the intensity of FLAIR images may present large anatomical deformations due to changes in the tissue perfusion, pressure, and lesion growth caused by the stroke, several attempts to use automatic image registration methods failed to accurately align the volumes. Instead, our framework utilized five landmark points placed manually at specific anatomical locations (center, plus four main cardinal directions) on the slice of the brain that had the largest ventricular area. An affine projection was applied to project the follow-up FLAIR and acute Tmax onto the original FLAIR image.

4) FLAIR Image Normalization and Ground Truth

Because the follow-up images were acquired with different settings and originated from different patients, their intensity values were not directly comparable. To allow for inter-patient comparisons, follow-up images were normalized with respect to the average intensities within the contralateral white matter. The normal-appearing white matter was delineated manually by an experienced researcher for both onset and follow-up brain volumes.

We obtained the ground truth tissue outcomes from an expert in neurology from UCLA who was asked to precisely delineate them infarcts manually, comparing the affected hemisphere with the contralateral hemisphere. Outlining was performed with the help of the commercially available medical imaging software 3D Doctor (http://www.ablesw.com/). At each pixel, the ground truth was set to 1 for infarction and 0 for no infarction.

5) Tmax Features

The Tmax parameter was computed on the acute images using software developed at UCLA, the Stroke Cerebral Analysis 2 (SCAN 2) package. SCAN 2 expresses the tissue contrast agent concentration C(t) as a convolution of the arterial input function (AIF) identified from the contralateral middle cerebral artery (MCA) and the residue function R(t) [4], C(t)=CBF×(AIF(t)⊗R(t)), where CBF is the cerebral blood flow. The residue function is obtained by deconvolution, and the time to its maximum value is used to specify Tmax. Therefore, Tmax is the arrival delay between the AIF and C(t).

6) Orientation Normalized Patch Sampling

In order to be able to predict tissue fate on a per-pixel basis, we randomly sampled a set of pixels from each image, and extracted a square patch of size 23 × 23 centered at each sampled pixel (as illustrated in Figure 1). Because the pose of the head varies from image to image, patches from different images are oriented at various angles relative to the head. Normalized orientation is desirable when comparing local image features across images [16], so we normalized the patches with respect to their orientation.

The patches were normalized with respect to the direction θ of the image gradient using a rotation performed with a bilinear interpolation (similarly to other works in computer vision [3]), (1)cM′=imrotate(cM,−θM)θM=tan−1Ly,Mσ(i,j)Lx,Mσ(i,j) where Lx,Mσ and Ly,Mσ are the Gaussian derivatives in x and y directions at the point (i,j) in the perfusion map M, (2)Lx,Mσ=∂∂xGσ⊗MLy,Mσ=∂∂yGσ⊗M where Gσ is a 2D isotropic Gaussian filter with standard deviation σ = 3 in our experiments.

Each patch was then paired with the label corresponding to its central pixel in the ground truth image. The resulting dataset consists of a set of orientation-normalized patches and their corresponding tissue fate labels.

C. Predictive Model1) Deep Learning

Deep learning is a field of machine learning that uses multiple layers of nonlinear processing units to model complex, nonlinear features in data [1]. It can produce very accurate results in tasks such as speech and image recognition [17], and it has been used successfully to approach problems in neuroimaging [20]. In a deep learning architecture, each layer models progressively higher-level features of the data. These features are learned during the process of training the model, and need not be specified ahead of time. Thus, deep learning allows for the automatic generation of a very high-level, abstract representation of data, even when it is not clear from the outset which will be the relevant features.

2) Convolutional Neural Networks

In this study, a deep learning method called a Convolutional Neural Network (CNN) [14] was used to generate a predictive model of tissue fate. This is a deep learning method inspired by the human visual system, specifically adapted to image recognition. It is designed to minimize training time and model complexity, and to provide translational invariance to image features. It achieves these design goals by feeding input images, or maps, forward through alternating convolutional layers and pooling layers. Convolutional layers convolve the input maps with a set of filters, or kernels, producing an output map for each kernel, for each input map. The parameters of these kernels are initialized to very small non-zero values, and during training, the parameters are adjusted via back-propagation over labeled examples to maximize the accuracy of the network–this is where the learning takes place. The network is able to learn features by which it can distinguish images from the different output classes. Pooling layers downsample the maps they are fed. This is not a learning step, it simply speeds up the training process without adding any parameters to the model, and it is this downsampling that provides translational invariance. The final layer assigns likelihoods for each output class, and is often a fully-connected neural network. Each cycle of one feed-forward and one back-propagation is referred to as a learning epoch.

3) Our Model

To construct our CNNs, We made use of DeepLearnToolbox, an open source set of Matlab libraries for deep learning algorithms [19]. In the deep learning community, there is no canonical method for determining the proper CNN configuration–that is, the optimal values of hyper-parameters such as number of layers and size of kernels for a given problem. When creating our CNNs, we selected hyper-parameters based on manual variation and observation. In order to maximize reproducibility and practical value, we selected hyper-parameters that would minimize computational complexity, where possible. The model developed in this study consists of two convolutional layers and two pooling layers, as illustrated in Figure 2. The dimensions of the kernels are 6 × 6. The output of the second pooling layer is unwound into a feature vector, and a linear classifier on that feature vector is used as a final layer. 100 learning epochs are performed. The model's input maps are the sampled Tmax patches; the model's output for each map, for each output class, is the probability that the map falls into that output class. A binary prediction is then obtained by selecting the output class with higher probability.

D. Experiments

To quantify the perfonnance of the deep learning model, it was used to predict the tissue outcomes of the 19 patients, and its results were evaluated against the manually-determined ground truths. As a point of comparison, a linear regression model was trained and evaluated in parallel.

For each patient, a network was trained on the combined labeled data of all other patients, in a leave-one-patient-out cross validation. It was then used to predict the tissue outcome for each of the patient's sampled Tmax patches, generating a prediction at each location in the patient's Tmax feature map. Those predictions were then evaluated against the ground truths.

A linear regression model was also trained for each patient, using the same leave-one-patient-out crossvalidation scheme. For this model, the ground truth labels were regressed against the mean values of their respective Tmax patches.

III. Results

After data pre-processing, there was evidence of lesions from previous strokes and/or unsuccessful perfusion processing in 6 of the 25 patients. These lesions had the potential to confound the results of the model, so the data for these patients was discarded.

The predictions of each model are visualized in Figure 3, in which the intensity of each pixel corresponds to the predicted probability of infarction at that location. Each image is labeled with its predictive accuracy, defined as number of correct binary predictions divided by total number of Tmax patches. The mean accuracy over the 19 patients for the deep learning model was 85.3 ± 9.1 %, and the mean accuracy for the linear regression model was 78.3 ± 5.5%.

IV. DiscussionA. Model Performance

Based on sheer accuracy, this deep learning model of tissue fate out-performs a linear, single-voxel-based model by a significant margin, when evaluated against the ground truth set by an expert neurologist.

We suspect that the heightened performance of this method is primarily a result of two factors. (1) At each point, it makes use of data from the surrounding region. This is important when analyzing noisy data, where predictions benefit greatly from being able to take the context of each voxel into account. (2) The nature of the neural network allows it to model a non-linear relationship between Tmax and tissue fate, and it is apparent from visually comparing the acute and follow-up images that their actual relationship is not entirely linear.

The CNN benefits from an advantage over other non-linear models, in that the precise mathematical relationship between acute Tmax and tissue fate does not need to be specified ahead of time. One typical disadvantage of the neural network approach is that training times can be long. However, for this application in a clinical setting, training time is not a large concern, as the network only needs to be trained once before it is deployed. Once trained, CNNs are computationally efficient to apply, and thus make optimal use of available computing power.

B. Future Directions

The model proposed here makes predictions based on two-dimensional input maps, as CNNs were specifically adapted to do. However, MRI provides data in three dimensions, and this additional information could potentially be used to increase predictive power, using a modified 3D CNN [11]. Furthermore, extensions of CNNs that take multi-channel data as inputs, RGB images for example, have been very successful [13]; in the case of MRI data, additional variables, such as FLAIR at symptom onset, could be incorporated into our model as channels alongside Tmax.

As CNNs have shown their potential not just for research but for clinical practice, there is an increasingly strong need for systematic investigation and standardization of hyper-parameter settings, which will accelerate development of applied deep learning methods. The evolution of the method developed here will continue to provide insight into the behavior of CNNs with respect to hyper-parameters in the medical imaging domain.

V. Conclusion

Our results indicate that tissue fate in ischemic stroke can be accurately forecasted by a relatively simple CNN at the time of symptom onset. We anticipate that the proposed improvements to our method will yield a clinically viable predictive tool to aid in stroke diagnosis and treatment decisions, ensuring that treatments such as clot-retrieval interventions are administered with confident knowledge of the associated risk and potential benefit.
