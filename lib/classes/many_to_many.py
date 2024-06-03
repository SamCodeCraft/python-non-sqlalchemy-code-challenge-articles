class Article:
    all = []  # Class-level list to keep track of all Article instances

    def __init__(self, author, magazine, title):
        self._check_title(title)
        self._check_author(author)
        self._check_magazine(magazine)

        self._title = title
        self.author = author
        self.magazine = magazine

        # Add the new article to the respective lists
        self.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    def _check_title(self, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string with 5 to 50 characters")

    def _check_author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")

    def _check_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._check_author(value)
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._check_magazine(value)
        self._magazine = value

class Author:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name
        self._articles = []  # List to hold articles written by the author

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles  # Returns all articles written by the author

    def magazines(self):
        # Returns a list of unique magazines the author has written for
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Association method: Create and associate a new Article instance
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        # Aggregate method: Returns a list of unique categories the author has written about
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all_magazines = []  # Class-level list to keep track of all Magazine instances

    def __init__(self, name, category):
        self._validate_name(name)
        self._validate_category(category)
        
        self._name = name
        self._category = category
        self._articles = []  # List to hold articles published in the magazine

        Magazine.all_magazines.append(self)  # Add the new magazine to the class-level list

    def _validate_name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string with 2 to 16 characters")

    def _validate_category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def articles(self):
        return self._articles  # Returns all articles published in the magazine

    def contributors(self):
        # Returns a list of unique authors who have written for the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Aggregate method: Returns a list of article titles in the magazine
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        # Aggregate method: Returns authors who have contributed more than 2 articles
        author_counts = {}
        for article in self._articles:
            if article.author not in author_counts:
                author_counts[article.author] = 0
            author_counts[article.author] += 1
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        # Class-level aggregate method: Returns the magazine with the most articles
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine._articles))
