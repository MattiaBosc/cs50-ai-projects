import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    model = {}
    links = len(corpus[page])
    
    for html_page in corpus:
        if not links:
            model[html_page] = 1 / len(corpus)
            continue
        model[html_page] = (1 - damping_factor) / len(corpus)
        if html_page != page and html_page in corpus[page]:
            model[html_page] += (damping_factor / links)
    
    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    model = {}
    for html_page in corpus:
        pagerank[html_page] = 0
        model[html_page] = transition_model(corpus, html_page, damping_factor)
        
    page = random.choice(list(corpus.keys()))
    for _ in range(n):
        choice = random.choices(list(model[page].keys()), weights = model[page].values(), k = 1)[0]
        pagerank[choice] += 1e-4
        page = choice
    
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    links = len(corpus)
    for html_page in corpus:
        pagerank[html_page] = 1 / links
        if len(corpus[html_page]) == 0:
            corpus[html_page] = corpus.keys()
    
    converged = False
    while not converged:
        for html_page in corpus:
            parents = []
            for page in corpus:
                if html_page in corpus[page]:
                    parents.append(page)
            summation = 0        
            for parent in parents:
                summation +=  pagerank[parent] / len(corpus[parent])
            current_rank = ((1 - damping_factor) / links) + (damping_factor * summation)
            
            if abs(pagerank[html_page] - current_rank) < 0.0001:
                converged = True
            
            pagerank[html_page] = current_rank

    return pagerank
   

if __name__ == "__main__":
    main()
