#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Union

from _exactextract import (FeatureSequentialProcessor as
                           _FeatureSequentialProcessor,
                           RasterSequentialProcessor as
                           _RasterSequentialProcessor, CoverageProcessor as
                           _CoverageProcessor)

from .dataset import GDALDatasetWrapper
from .raster import GDALRasterWrapper
from .operation import Operation
from .writer import MapWriter, GDALWriter, CoverageWriter


class FeatureSequentialProcessor(_FeatureSequentialProcessor):
    """ Binding class around exactextract FeatureSequentialProcessor """

    def __init__(self, ds_wrapper: GDALDatasetWrapper,
                 writer: Union[MapWriter,
                               GDALWriter], op_list: List[Operation]):
        """
        Create FeatureSequentialProcessor object

        Args:
            ds_wrapper (GDALDatasetWrapper): Dataset to use
            writer (Union[MapWriter, GDALWriter]): Writer to use
            op_list (List[Operation]): List of operations
        """
        super().__init__(ds_wrapper, writer, op_list)


class RasterSequentialProcessor(_RasterSequentialProcessor):
    """ Binding class around exactextract RasterSequentialProcessor """

    def __init__(self, ds_wrapper: GDALDatasetWrapper,
                 writer: Union[MapWriter,
                               GDALWriter], op_list: List[Operation]):
        """
        Create RasterSequentialProcessor object

        Args:
            ds_wrapper (GDALDatasetWrapper): Dataset to use
            writer (Union[MapWriter, GDALWriter]): Writer to use
            op_list (List[Operation]): List of operations
        """
        super().__init__(ds_wrapper, writer, op_list)


class CoverageProcessor(_CoverageProcessor):
    """ Binding class around exactextract FeatureSequentialProcessor """

    def __init__(self, ds_wrapper: GDALDatasetWrapper, writer: CoverageWriter,
                 raster: GDALRasterWrapper):
        """
        Create CoverageProcessor object

        Args:
        ds_wrapper (GDALDatasetWrapper): Dataset to use
            writer (CoverageWriter): Writer to use (must be CoverageWriter)
            raster (GDALRasterWrapper): Raster for coverage fraction
        """
        super().__init__(ds_wrapper, writer, raster)