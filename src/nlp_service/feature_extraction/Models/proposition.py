from feature_extraction.Models import clause, compliment, predicate

'''
LOGIC MODEL
---------------------------------------------
Contains clauses, predicates and compliments
'''


class PropositionModel:
    def __init__(self):
        self.clause = clause.Clause()
        self.predicate = predicate.Predicate()
        self.compliment = compliment.Compliment()
        self.category = []
        self.previous = None
        self.next = None

    #############################################
    # CATEGORY MATCH
    # -------------------------------------------
    # Returns true if any element of the proposition
    # matches the word category
    #
    # category: String
    def category_match(self, category):
        if self.compliment.category_match(category):
            self.category.append(category)
            return True
        elif self.predicate.category_match(category):
            self.category.append(category)
            return True
        elif self.clause.category_match(category):
            self.category.append(category)
            return True
        return False

    ################################################
    # CONTAIN TAG
    # ----------------------------------------------
    # Returns true if any element of the proposition
    # contain a word with a certain tag
    #
    # tag: string
    def contains_tag(self, tag):
        if self.clause.get_element_from_tag(tag) is not None:
            return True
        if self.predicate.get_element_from_tag(tag) is not None:
            return True
        if self.compliment.get_element_from_tag(tag) is not None:
            return True
        return False

    ################################################
    # GET TAGGED WORD
    # ----------------------------------------------
    # Returns a list of words with a certain tag
    #
    # tag: String
    def get_tagged_word(self, tag):
        lst = []
        a = self.clause.get_element_from_tag(tag)
        if a is not None:
            lst += a

        a = self.predicate.get_element_from_tag(tag)
        if a is not None:
            lst += a

        a = self.compliment.get_element_from_tag(tag)
        if a is not None:
            lst += a
        return lst

    def __ne__(self, other):
        return not (self.__eq__(other))

    def __str__(self):
        return str(self.clause) + "\n" + str(self.predicate) + "\n" + str(self.compliment)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        elif self.clause != other.clause:
            return False
        elif self.predicate != other.predicate:
            return False
        elif self.compliment != other.compliment:
            return False
        return True
