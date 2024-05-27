class Article:
            all = []

            def __init__(self, author, magazine, title):
                if not isinstance(title, str) or not (5 <= len(title) <= 50):
                    print("Title must be a string with 5 to 50 characters")
                if not isinstance(author, Author):
                    print("Author must be an instance of Author")
                if not isinstance(magazine, Magazine):
                    print("Magazine must be an instance of Magazine")

                self._title = title if isinstance(title, str) and 5 <= len(title) <= 50 else None
                self.author = author if isinstance(author, Author) else None
                self.magazine = magazine if isinstance(magazine, Magazine) else None

                if self._title and self.author and self.magazine:
                    self.all.append(self)
                    author._articles.append(self)
                    magazine._articles.append(self)

            @property
            def title(self):
                return self._title

            @property
            def author(self):
                return self._author

            @author.setter
            def author(self, value):
                if not isinstance(value, Author):
                    print("Author must be an instance of Author")
                    return
                self._author = value

            @property
            def magazine(self):
                return self._magazine

            @magazine.setter
            def magazine(self, value):
                if not isinstance(value, Magazine):
                    print("Magazine must be an instance of Magazine")
                    return
                self._magazine = value

class Author:
            def __init__(self, name):
                if not isinstance(name, str) or len(name) == 0:
                    print("Name must be a non-empty string")
                    self._name = None
                else:
                    self._name = name
                self._articles = []

            @property
            def name(self):
                return self._name

            def articles(self):
                return self._articles

            def magazines(self):
                return list(set(article.magazine for article in self._articles))

            def add_article(self, magazine, title):
                if not isinstance(magazine, Magazine):
                    print("Magazine must be an instance of Magazine")
                    return
                article = Article(self, magazine, title)
                if article.title and article.author and article.magazine:
                    return article

            def topic_areas(self):
                if not self._articles:
                    return None
                return list(set(article.magazine.category for article in self._articles))

class Magazine:
            def __init__(self, name, category):
                if not isinstance(name, str) or not (2 <= len(name) <= 16):
                    print("Name must be a string with 2 to 16 characters")
                    self._name = None
                else:
                    self._name = name
                if not isinstance(category, str) or len(category) == 0:
                    print("Category must be a non-empty string")
                    self._category = None
                else:
                    self._category = category
                self._articles = []

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                if not isinstance(value, str) or not (2 <= len(value) <= 16):
                    print("Name must be a string with 2 to 16 characters")
                    return
                self._name = value

            @property
            def category(self):
                return self._category

            @category.setter
            def category(self, value):
                if not isinstance(value, str) or len(value) == 0:
                    print("Category must be a non-empty string")
                    return
                self._category = value

            def articles(self):
                return self._articles

            def contributors(self):
                return list(set(article.author for article in self._articles))

            def article_titles(self):
                titles = [article.title for article in self._articles]
                return titles if titles else None

            def contributing_authors(self):
                author_counts = {}
                for article in self._articles:
                    if article.author not in author_counts:
                        author_counts[article.author] = 0
                    author_counts[article.author] += 1
                return [author for author, count in author_counts.items() if count > 2] or None
                magazine._articles.append(self)

   