# py.test -k "p2"
#  py.test --timeout=10 --timeout_method=thread -k "v2"

from impl import Queue
import hypothesis.strategies as st
from hypothesis import given
import pytest
import math

class TestQueue(object):

    valid = st.lists(elements=(st.floats(allow_infinity=False, allow_nan=False) | st.text() | st.integers() | st.booleans() | st.characters()))
    #invalid = st.lists(elements=(st.floats(allow_infinity=True, allow_nan=True) | st.text() | st.integers | st.booleans | st.characters))

    def test_queue_init(self):
        try:
            queue = Queue()
            assert True
        except:
            assert False
        pass

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

    @pytest.mark.timeout(2, 'thread')
    def test_first_element_in_is_first_element_out(self):
        queue = Queue()
        queue.enqueue(143)
        queue.enqueue(2)
        queue.enqueue(3)
        try:
            if queue.dequeue() is 143:
                assert True
            else:
                assert False
        except:
            assert False

    @given(valid)
    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_element_increase_len_by_one(self, list):
        queue = Queue()
        length = queue.len()
        try:
            for element in list:
                queue.enqueue(element)
                if (length+1) is queue.len():
                    length = length + 1
                else:
                    assert False
            assert True
        except:
            assert False
        pass

    @given(valid)
    @pytest.mark.timeout(2, 'thread')
    def test_dequeue_element_decrease_len_by_one(self, list):
        queue = Queue()
        for element in list:
            queue.enqueue(element)
        length = queue.len()
        try:
            for element in range(0, len(list)+5):
                if(queue.dequeue() is None):
                    if length is not queue.len():
                        assert False
                else:
                    if (length-1) is queue.len():
                        length = length - 1
                    else:
                        assert False
            assert True
        except:
            assert False
        pass

    @given(valid)
    @pytest.mark.timeout(2, 'thread')
    def test_enqueue_list_dequeue_list_equals_list(self, list):
        #push list onto queue
        #dequeue list onto queue
        #check that dequeued list is original list
        queue = Queue()
        newList = []
        for element in list:
            queue.enqueue(element)
        for element in range(0,len(list)):
            newList.append(queue.dequeue())
        try:
            if newList == list:
                assert True
            else:
                assert False
        except:
            assert False

        pass

    @pytest.mark.timeout(2, 'thread')
    def test_len_always_positive(self):
        queue = Queue()
        queue.enqueue(1)
        for element in range(0,10):
            queue.dequeue()
        try:
            if queue.len() < 0:
                assert False
            else:
                assert True
        except:
            assert False

    @pytest.mark.timeout(2, 'thread')
    def test_dequeue_empty_queue_does_not_change_len(self):
        queue = Queue()
        while queue.len() > 0:
            queue.dequeue()
        length = queue.len()
        if(length is 0):
            try:
                queue.dequeue()
                if(length is not queue.len()):
                    assert False
                else:
                    assert True
            except:
                assert False
        else:
            assert False

    #11) Length of stack equals to # of successful pushes - # of successful pops
    @given(valid)
    @pytest.mark.timeout(2, 'thread')
    def test_len_equals_enqueue_minus_dequeue(self, list):
        queue = Queue()
        length = queue.len()
        try:
            for element in list:
                queue.enqueue(element)
                if((length+1) is not queue.len()):
                    assert False
                length = length + 1
            for element in list:
                queue.dequeue()
                if((length-1) is not queue.len()):
                    assert False
                length = length - 1
            assert True
        except:
            assert False