Cluster_and_Classification
==========================
CSCE 670 :: Information Storage and Retrieval :: Spring 2013

Homework 3: Due: April 7, 2013

Learning objectives:

Working with a web API
Clustering
Classification
Evaluation
Part 0: Getting Started with the Bing Search API

For this homework, you'll be working with Bing's search API to explore different techniques for clustering and classification. To begin with, you need to get a Bing Search API key so that you can use the service.

Start by signing up at Microsoft's Azure datamarket; you should sign up the free version which allows for 5,000 transactions each month.

To get familiar, you can simply construct a URL like:

https://user:yourAppKey@api.datamarket.azure.com/Bing/Search/News?Query=%27bing%20is%20good%27&$format=json&$top=10
which provides the first 10 results from Bing for the query "bing is good", restricting to news results. You should replace "yourAppKey" with -- surprise -- your Bing Search API key. In this homework, we will use only "News" results from Bing. Notice in the URL the use of "News" to limit the search results to News.

With your key, you can directly access Bing Search results in a "programmatic" way from within Python. You'll find many resources to help you get started here:

http://hackertarget.com/bing-azure-api-python-ubuntu
https://github.com/xthepoet/pyBingSearchAPI
http://gavinmhackeling.com/blog/2012/05/using-the-bing-search-api-in-python
https://code.google.com/p/pybing
Requests Module
as well as more official documentation provided by Microsoft:

Bing API Quick Start and Code Samples
Bing API FAQ
Bing API Schema Guide
You may find that configuring your URLs is a little bit tricky. We suggest that you try in your browser first to refine your URL format, and then write your Python code. If you're still having trouble, there are tons of well-written code examples online, and we encourage you to communicate with others on the Google Group.

Part 1: Clustering Query Results aka Clusty to the Rescue!

Once you feel comfortable interacting with the Bing Search API and parsing the JSON-formatted results, you should turn your sights to clustering. Your goal in this part is to build a clustering search engine, much like the Clusty search engine.

As you may have noticed, the search results returned by the Bing Search API are some snippets of retrieved pages, including title information and description for each page. You should treat each snippet (title + description) as a single document. You will write a clustering engine that issues queries and then clusters the returned results.

Concretely, we're going to focus on just 5 queries and the first 30 returned results for each query:

texas aggies
texas longhorns
duke blue devils
dallas cowboys
dallas mavericks
In total, you should collect a maximum of 150 documents. Over this collection of documents, you should find clusters using the k-means clustering algorithm. As a baseline, you should represent each document by a vector, where terms are weighted by their TF-IDF values. You should tokenize based on whitespace and punctuation. Do not remove stop words. Apply casefolding.

When you build your clustering engine, you should write your own core clustering functionality; do not import or reuse any existing packages!

Now you're going to evaluate the quality of your clustering engine. Since we have the true "classes" of the documents (based on the five queries: we know that 30 documents belong to the class "texas aggies", 30 belong to the class "texas longhorns" and so forth), you can evaluate the quality of your clusters using an external criterion. We're going to use Purity and RI (Rand Index).

What we expect in your write-up:

You should experiment with different values of k, using random re-starts to find the best clusters for each k (as measured by RSS). Show us a graph comparing k vs. RSS. Is there a knee in the curve?
For your best clusters for each k, evaluate their quality using Purity and RI. Show us a graph comparing k vs. Purity and k vs. RI. What do you observe?
You should explain for at least one of your k values how you arrived at your Purity and RI scores. Show us enough detail so that we can understand your calculations. Do not just list your final number.
Part 2: Classification

You're now going to build a classification component to go with your clustering engine. If you dig through the Bing Search API documentation, you'll see that there's a parameter called "NewsCategory" that allows for results to be limited to just particular categories: business, entertainment, sports, and so on. For now, let's focus on three categories: entertainment, business, and politics. You can do that by augmenting your URLs with "&NewsCategory=%27rt_Entertainment%27", "&NewsCategory=%27rt_Business%27", or "&NewsCategory=%27rt_Politics%27".

You're going to build a training set by issuing the following queries to all three categories:

bing, amazon, twitter, yahoo, google
beyonce, bieber, television, movies, music
obama, america, congress, senate, lawmakers
You should issue each query to each of those 3 categories, and collect at maximum 30 results. Each category should have at most 450 documents (15 queries * 30 results). In total, you should have at most 1350 documents (450 documents per category * 3 categories). (Most likely, you should have fewer than 1350 documents since some queries will not return 30 documents).

Based on this training data, you should build a Naive Bayes classifier following our treatment in class. Use add-one smoothing.

To test the quality of your Naive Bayes classifier, we need a testing set. You should issue the following five queries to all three categories:

amazon, apple, facebook, westeros, gonzaga, banana
You should issue each query to each of those 3 categories, and collect at maximum 30 results. Use the category associated with the search result as its ground truth class. Your task is to assign a label (Entertainment, Business, Politics) to each document (i.e., each query result) using your Naive Bayes classifier.

Since you have the ground truth class of each result, you can directly compare your predicted label with its actual label.

What we expect in your write-up:

You should report the microaveraged F1 for your classification results. Be sure to report the 2x2 confusion matrix for your classifiers.
You should explain for at least one of your microaveraged F1 values how you arrived at your score. Show us enough detail so that we can understand your calculations. Do not just list your final number.
Part 3: To Infinity and Beyond!

For this final task, you are going to experiment with different approaches for improving your clustering and classification results. This part is completely open-ended. You may choose to represent your documents differently (e.g., use new weighting schemes, use different features, use feature selection), implement a fancy new classifier, etc.

Your goal is to provide an "improved version" that results in better results for your clustering and for your classification result. We leave the details to you; but creativity is always appreciated.

You may find that a single change (e.g., document representation) improves both clustering and classification. Or you may find that specific changes are needed to improve clustering, but different changes are needed to improve classification. Either way, you should clearly argue for your improvements!

What we expect in your write-up:

You should show us comparison figures of your baseline method (from Part 1 and Part 2) versus your new, improved method. Show us (at least) one figure for classification and (at least) one for clustering.
Include in your report a brief explanation about why your advanced version (or versions!) is indeed more advanced than the basic version, e.g. a better weighting scheme to represent a snippet? Implement other fancy classfication methods? Don't forget to describe and explain your improvements in the report.
What to Turn In:

As you may have found, this time not every one has the same dataset. So, we require you write your collected data (either parsed or raw data) into local files in whatever format, and your code should read data from those local files (don't make your code call API everytime you run your program). Submit your data along with code and report.
You should use the turnin homework submission system at https://csnet.cs.tamu.edu/. You should see an option to submit "Homework 3" associated with CSCE 670.
We expect a single zip file containing your complete Python code, collected dataset, a readme file about how to compile, run, and test your program, and a SHORT REPORT. In the report, you should at least include the complete evaluation results and brief descriptions of your implementations of baseline and improving methods. Screenshots are welcome. PDF only please.
Grading Rubrics

We will give some credit for the code itself, so please make your code clear and readable and be aware of the importance of code documentation.

Part 1: 30 points
Part 2: 30 points
Part 3: 30 points
Code readability: 5 points
Report quality: 5 points
