#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exactextract import GDALDatasetWrapper, GDALRasterWrapper, CoverageProcessor, CoverageWriter

if __name__ == '__main__':

    # Define dataset wrapper
    dsw = GDALDatasetWrapper('./python/tests/data/simple_multilayer.gpkg')

    # Define raster wrapper
    rsw = GDALRasterWrapper('./python/tests/data/simple_raster.tif')

    # Define operations
    # TODO: shouldn't this op be a possible input to Feature/Raster SequentialProcessors?
    # op = Coverage(raster=rsw)

    # Define output writer
    writer = CoverageWriter('./coverage_output.json', dsw)

    # Process the data!
    processor = CoverageProcessor(dsw, writer, rsw)
    processor.process()

    # Flush changes to disk
    writer = None