from markovgen import Markov
from unittest import TestCase

class MarkovgenTests(TestCase):
    def testForward(self):
        self.assertRaises(ValueError, Markov().generate_markov_text)
        for x in range(1, 1000):
            l = Markov(['foo bar baz qux']).generate_markov_text()
            self.assertIn(l, ['foo bar baz qux', 'bar baz qux', 'baz qux'])

    def testBackward(self):
        self.assertRaises(ValueError, Markov().generate_markov_text)
        for x in range(1, 1000):
            l = Markov(['foo bar baz qux']).generate_markov_text(backward=True)
            self.assertIn(l, ['foo bar baz qux', 'foo bar baz', 'foo bar'])

    def testForceSeedForward(self):
        for x in range(1, 1000):
            l = Markov(['foo bar baz qux']).generate_markov_text(
                    seed='bar')
            self.assertIn(l, ['bar baz qux'])
        for x in range(1, 1000):
            l = Markov(['foo bar bar baz qux']).generate_markov_text(
                    seed=('bar', 'baz'))
            self.assertIn(l, ['bar baz qux'])

    def testForceSeedBackward(self):
        for x in range(1, 1000):
            l = Markov(['foo bar baz qux']).generate_markov_text(
                    seed='bar', backward=True)
            self.assertIn(l, ['foo bar'])

    def testAvailableSeeds(self):
        l = Markov(['foo bar baz qux']).available_seeds()
        l = {x for x in l if '\n' not in x}
        self.assertEqual(l, {('foo', 'bar'), ('bar', 'baz'), ('baz', 'qux')})
        l = Markov(['foo bar baz qux']).available_seeds(backward=True)
        l = {x for x in l if '\n' not in x}
        self.assertEqual(l, {('qux', 'baz'), ('baz', 'bar'), ('bar', 'foo')})

