#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include "processor_bindings.h"
#include "gdal_dataset_wrapper.h"
#include "output_writer.h"
#include "processor.h"
#include "feature_sequential_processor.h"
#include "raster_sequential_processor.h"
#include "coverage_processor.h"

namespace py = pybind11;

namespace exactextract
{
    void bind_processor(py::module &m)
    {
        py::class_<Processor>(m, "Processor")
            .def("process", &Processor::process)
            .def("set_max_cells_in_memory", &Processor::set_max_cells_in_memory, py::arg("n"))
            .def("show_progress", &Processor::show_progress, py::arg("val"));

        py::class_<FeatureSequentialProcessor, Processor>(m, "FeatureSequentialProcessor")
            .def(py::init<GDALDatasetWrapper &, OutputWriter &, const std::vector<Operation> &>())
            .def("process", &FeatureSequentialProcessor::process);

        py::class_<RasterSequentialProcessor, Processor>(m, "RasterSequentialProcessor")
            .def(py::init<GDALDatasetWrapper &, OutputWriter &, const std::vector<Operation> &>())
            .def("read_features", &RasterSequentialProcessor::read_features)
            .def("populate_index", &RasterSequentialProcessor::populate_index)
            .def("process", &RasterSequentialProcessor::process);

        py::class_<CoverageProcessor, FeatureSequentialProcessor>(m, "CoverageProcessor")
            .def(py::init([](GDALDatasetWrapper &dsw, OutputWriter &out, GDALRasterWrapper &rsw)
                          {
            std::unordered_map<std::string, GDALRasterWrapper> rasters;
            rasters.emplace("", std::move(rsw)); // TODO: couldn't figure out how to just include this in the constructor
            return std::make_unique<CoverageProcessor>(dsw, out, rasters); }))
            .def("process", &CoverageProcessor::process);
    }
}