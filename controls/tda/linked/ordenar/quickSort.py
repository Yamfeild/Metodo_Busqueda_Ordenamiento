import random
class QuickSort:
    def sort_primitive_ascendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[random.randint(0, len(array) - 1)]
            less = [i for i in array if i < pivot]
            equal = [i for i in array if i == pivot]
            greater = [i for i in array if i > pivot]
            return self.sort_primitive_ascendent(less) + equal + self.sort_primitive_ascendent(greater)

    def sort_primitive_descendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[random.randint(0, len(array) - 1)]
            less = [i for i in array if i < pivot]
            equal = [i for i in array if i == pivot]
            greater = [i for i in array if i > pivot]
            return self.sort_primitive_descendent(greater) + equal + self.sort_primitive_descendent(less)

    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if getattr(x, attribute) <= getattr(pivot, attribute)]
        greater = [x for x in array[1:] if getattr(x, attribute) > getattr(pivot, attribute)]
        return self.sort_models_ascendent(less, attribute) + [pivot] + self.sort_models_ascendent(greater, attribute)

    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if getattr(x, attribute) >= getattr(pivot, attribute)]
        greater = [x for x in array[1:] if getattr(x, attribute) < getattr(pivot, attribute)]
        return self.sort_models_descendent(less, attribute) + [pivot] + self.sort_models_descendent(greater, attribute)