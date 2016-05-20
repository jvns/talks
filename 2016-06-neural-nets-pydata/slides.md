# 

<h1>how to trick a neural network </h1>

<h2> (or: be skeptical of machine learning) </h2>

by Julia Evans <br>
Stripe <br>


* twitter: @b0rk <br>
* blog: jvns.ca

<br>
notes at http://bit.ly/trick-neural-network

[github]: https://github.com/jvns
[twitter]:  https://twitter.com/b0rk
[website]: http://jvns.ca

<br><br>

# ❤ machine learning <br> 😒 machine learning


# about me

* machine learning @ stripe
* stop credit card fraud

# what is machine learning?

# 

* john: probably american
* jean: probably french
* johannes: probably german

# 

<h2> data </h2>

<div style="font-size: 24px">

john - american | john - brazilian | john - american | julia - american
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| andy - british | andy - american | andy - canadian
</div>

# model

* julia: american (probability = 60%)
* johannes: german (probability = 70%)
* john: american (probability = 40%)
* jean: french (probability = 50%)

# your model is only as good as your data

# fun with machine learning

# neural networks

# 

<img src="alphago.png">

# step 0: be confused about neural networks

</section>

<section data-background="beaches.png">

</section>

<section data-background="cars.png">

</section>

<section data-background="fire_hydrant.png">
</section>

<section data-background="baby.png">
</section>


<!-- "this is what we're going to talk about" -->

# step 1: read a cool paper


<img src="paper.png">


# neural networks aren't magic: they're math

# i have a math degree i can do this =D

# what the paper said

<img src="panda.png">

# what the paper said

<img src="trick.png">

# can I implement the paper???

# yes

# the code for this is is all an ipython notebook

# a neural network is a function

# 

<img src="corgi.png" width=50%>

# 

<img src="corgi-input.png" width=30%>
<img src="labels.png" width=60%>



</section>

<section data-background="cat_data_ndarray.png">

</section>

# step 2: spend 10 hours setting up neural network software

# step 3: download the neural network in the paper

</section>

<section data-background="download_neural_network.png">

</section>

# 50 megabytes


# step 4: PREDICT SOME THINGS WITH IT

</section>

<section data-background="sword.png">

</section>

<section data-background="kitten.png">

</section>

<section data-background="trash.png">

</section>

<section data-background="queen.png">

# step 5: trick it

# step 4.5: be very confused about neural networks



# back to math for a second

# 

<img src="hill.jpg" width=100%>

# 

<img src="hill-with-panda.jpg" width=100%>

# 

<img src="hill-with-arrow.jpg" width=100%>

# which direction do we take the image in?

# best direction = derivative

# derivative = backpropagation

# 

<img src="black.png" width=100%>

#

<img src="paper_towel_gradient.png" width=100%>

</section>

# 

<img src="black2.png" width="80%">


#

</section>

<section data-background="paper_towel_velvet.png">

</section>

# 

<img src="black_paper_towel.png" width="80%">

# 

<img src="paper_towel_magnified.png" width="80%">


# let's do more!!

# 

<img src="garbage_can.png" width="80%">

# 

<img src="garbage_can_gradient.png" width="80%">

# 

<img src="kitten_bath_towel.png" width="80%">


# 

<img src="kitten_bath_towel_difference.png" width="80%">


# panda -> vulture

</section>

<section data-background="panda_vulture_graph.png">

</section>

#

<img src="trick.png">

# 

<pre style="font-size:10px; margin: -40px; margin-left: -80px;">
caffe.set_mode_cpu()

# Load our model! trained by the GOOGLES! <3
def load_model():
    BATCH_SIZE = 1
    net = caffe.Net('/opt/caffe/models/bvlc_googlenet/deploy.prototxt',
                    '/models/bvlc_googlenet.caffemodel',
                    caffe.TEST)
    # change batch size to 1 for faster processing
    # this just means that we're only processing one image at a time instead of like 50
    shape = list(net.blobs['data'].data.shape)
    shape[0] = BATCH_SIZE
    net.blobs['data'].reshape(*shape)
    net.blobs['prob'].reshape(BATCH_SIZE, )
    net.reshape() 
    return net
net = load_model()
# Caffe comes with a handy transformer pipeline so that
# we can make our images into the format it needs! Yay!
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
def display(data):
    plt.imshow(transformer.deprocess('data', data))
def get_label_name(num):
    options = labels[num].split(',')
    # remove the tag
    options[0] = ' '.join(options[0].split(' ')[1:])
    return ','.join(options[:2])
def predict(data, n_preds=6, display_output=True, display_image= True):
    net.blobs['data'].data[...] = data
    display(data)
    prob = net.forward()['prob']
    probs = prob[0]
    prediction = probs.argmax()
    top_k = probs.argsort()[::-1]
    for pred in top_k[:n_preds]:
        percent = round(probs[pred] * 100, 2)
        # display it compactly if we're displaying more than the top prediction
        pred_formatted = "%03d" % pred
        format_string = "label: {cls} ({label})\ncertainty: {certainty}%"
        print format_string.format(
            cls=pred_formatted, label=get_label_name(pred), certainty=percent)
    return prob
def compute_gradient(image, intended_outcome):
    predict(image, display_output=False)
    # Get an empty set of probabilities
    probs = np.zeros_like(net.blobs['prob'].data)
    # Set the probability for our intended outcome to 1
    probs[0][intended_outcome] = 1
    # Do backpropagation to calculate the gradient for that outcome
    gradient = net.backward(prob=probs)
    return gradient['data'].copy()
def trick(image, desired_output, n_steps=1):
    # maintain a list of outputs at each step
    prediction_steps = []
    for _ in range(n_steps - 1):
        preds = predict(image, display_output=False)
        prediction_steps.append(np.copy(preds))
        grad = compute_gradient(image, desired_output) # paper towel
        delta = np.sign(grad)
        # If there are n steps, we make them size 1/n -- small!
        image = image + delta * 0.9 / n_steps
    return image, prediction_steps
</pre>

# 

```
def trick(image, desired_output, n_steps=1):
    for _ in range(n_steps - 1):
        grad = compute_gradient(image, desired_output) # paper towel
        delta = np.sign(grad)
        # If there are n steps, we make them 
        # each size 1/n -- small!
        image = image + delta * 0.9 / n_steps
    return image, prediction_steps
```

# what you can do next

* read the paper!
* play with the neural net yourself!
* michael nielsen's neural networks book

# papers we love

#

<h1 style="text-transform:none"> http://bit.ly/trick-neural-network</h1>

# if we can trick a neural network, maybe we can understand it

# ok, so machine learning is cool

# machine learning is also *important*

(otherwise i would never get paid to do it)

# 

* photo classification
* spam filtering
* approving your loan application

# reasons to be skeptical of machine learning

# 1. only as good as the data you put into it

# 

<h2> data </h2>

<div style="font-size: 24px">

john - american | john - brazilian | john - american | julia - american
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american 
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| andy - british | andy - american | andy - canadian
| julia - canadian | julia - australian | julia - american | julia - american | johannes - german | johannes - german | johannes - german | johannes - american
| andy - british | andy - american | andy - canadian
</div>

# what if you forget the data from china?

# 2. programs often have bugs

# 2. machine learning programs often have bugs 

# 

<h1 style="text-transform:none"> Machine Learning: The High Interest Credit Card of Technical Debt </h1>

# 3. you didn't tell your model about people


#

<img src="queen.png" width="80%">

# 4. sometimes it just doesn't work


label: baby
<img src="donald-trump-pinata.png" width="80%">

<!-- ml is only *supposed* to work like 90% of the time anyway-->

# ... or it has unexpected consequences


</section>

<section data-background="insightful.jpg">
</section>

#

<h1 style="text-transform:lowercase"> "Consequences of an insightful algorithm" <br> Carina Zona @cczona</h1>

# be skeptical <br> & <br> ask questions

<!-- maybe say the pork in a muslim country here -->


# okay, I found something weird. how do I debug it?

# ★★★ <br> magically guess <br> ★★★


# 

<h1 style="text-decoration:line-through">

★★★ <br> magically guess <br> ★★★
</h1>

# 1. look at the model

# 

income = 1000 * age + 10000 * gender

# 

<img src="titanic.png" width="80%">

# 

<img src="decision_tree.png" width="80%">

# 2. make two models

1. model your data with a complicated model
1. model your complicated model with a simple model

# 3. talk to an academic

* PhD students = AMAZING
* NIPS = really fun

# it's math, <br>not magic

# simple systems can work incredibly well

❤❤❤ linear models ❤❤❤

# 

<h1 style="text-transform:none">
you can trick a neural network
</h1>

# 

<h1 style="text-transform:none">
thanks! <br><br>

twitter: @b0rk <br>
blog: jvns.ca
</h1>
