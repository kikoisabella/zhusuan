#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
import warnings

from zhusuan.distributions.base import *


__all__ = [
    'ExponentialFamily',
]

class ExponentialFamily(Distribution):
    """
    Providing the support of the exponential family.
    """
    def __init__(self,
                 dtype,
                 param_dtype,
                 is_continuous,
                 natural_param,
                 Z,
                 is_reparameterized,
                 use_path_derivative=False,
                 group_ndims=0,
                 **kwargs
                 ):
        self._natural_param = natural_param
        self._Z = Z
        super(ExponentialFamily, self).__init__(
            dtype=dtype,
            param_dtype=param_dtype,
            is_continuous=is_continuous,
            is_reparameterized=is_reparameterized,
            use_path_derivative=use_path_derivative,
            group_ndims=group_ndims,
            **kwargs)

    @property
    def natural_param(self):
        """The natural parameter of the distribution."""
        return self._natural_param

    @property
    def Z(self):
        """The normalization parameter of the distribution."""
        return self._Z
