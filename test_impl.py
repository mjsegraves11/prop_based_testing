from impl import Queue
import hypothesis.strategies as st
from hypothesis import given
import pytest
import math

class TestQueue(object):

    valid = st.lists(elements=(st.floats(allow_nan=False) | st.text() | st.integers() | st.booleans() | st.characters()))
    #invalid = st.lists(elements=(st.floats(allow_infinity=True, allow_nan=True) | st.text() | st.integers | st.booleans | st.characters))

    @pytest.mark.timeout(2, 'thread')
    def test_len_when_queue_init(self):
        queue = Queue()
        try:
            assert queue.len() is 0
        except:
            assert False
        pass

    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_when_queue_init(self):
        queue = Queue()
        try:
            queue.enqueue(23)
            assert True
        except:
            assert False
        pass

    @pytest.mark.timeout(2, 'thread')
    def test_dequeue_when_queue_init(self):
        queue = Queue()
        try:
            element = queue.dequeue()
            if(element is None):
                assert True
            else:
                assert False
        except:
            assert False

    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_with_invalid_input_None(self):
        queue = Queue()
        try:
            queue.enqueue(None)
            assert False
        except ValueError:
            assert True
        except:
            assert False

    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_with_invalid_input_Nan(self):
        queue = Queue()
        try:
            queue.enqueue(float('Nan'))
            assert False
        except ValueError:
            assert True
        except:
            assert False

    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_with_invalid_input_Inf(self):
        queue = Queue()
        try:
            queue.enqueue(float('Inf'))
            assert False
        except ValueError:
            assert True
        except:
            assert False


    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_with_invalid_input_Neg_Inf(self):
        queue = Queue()
        try:
            queue.enqueue(float('-Inf'))
            assert False
        except ValueError:
            assert True
        except:
            assert False

    #1) If len() > 0 and x = pop(), then x was the last item pushed and remove x from stack
    #2) If nothing has be placed on the stack, then len() = 0
    #3) Calls to successful push should increment length by 1
    #4) Calls to successful (non-None) pop should decrement length by 1
    #5) Popping an empty stack returns None
    #6) push(None) results in ValueError exception
    #7) n number of successful pushes followed by n number of successful pops, values pushed should be observed in reverse order when popped
    #8) len should always return non-negative integer
    #9) Popping and empty stack doesn’t change length
    #10) If len() > 0, then pop() return None
    #11) Length of stack equals to # of successful pushes - # of successful pops

    @given(valid)
    @pytest.mark.timeout(2, 'thread')
    def test(self, li):
        #information for what to do for test

        # 8====D~~~~ __/`````\`O

        assert 1 > 0
        pass































