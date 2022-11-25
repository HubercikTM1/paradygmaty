import paradygmaty

class AnimalTest():
    def functionTest(self):
        """
        Test konstkruktora
        >>> a = paradygmaty.cat("maincoon", 25, "green")

        >>> a.desc()
        mój gatunek to maincoon!

        >>> a.scratch()
        drapu drapu
        >>> a.speak()
        miau
        >>> a.run()
        biegne 25 km/h! jestem prendkościom!

        >>> b=paradygmaty.dog("mops",60,"black")

        >>> b.desc()
        mój gatunek to mops!
        >>> b.speak()
        hau
        >>> b.hunt()
        dogonię cie
        >>> b.rainbow()
        mój kolor to black
        >>> 1 + 1 == 2
        True



        """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
