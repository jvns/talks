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

# what you can do next

* read the paper!
* play with the neural net yourself!
* michael nielsen's neural networks book

# papers we love

#

<h1 style="text-transform:lowercase"> http://bit.ly/trick-neural-network</h1>

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

## understand nothing <br> ⇝ understand something ⇜ <br> understand everything

# thanks!

* twitter: @b0rk <br>
* blog: jvns.ca
