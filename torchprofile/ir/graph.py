__all__ = ['Graph']


class Graph:
    def __init__(self, tensors, inputs, outputs, nodes):
        self.tensors = tensors
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = nodes

    @property
    def tensors(self):
        return self._tensors

    @tensors.setter
    def tensors(self, tensors):
        self._tensors = tensors

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        self._inputs = inputs

    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        self._outputs = outputs

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes

    def __str__(self):
        return '\n'.join([str(node) for node in self.nodes])
