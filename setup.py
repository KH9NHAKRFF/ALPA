from setuptools import setup, find_packages
from torch.utils import cpp_extension

setup(name='alpa',
      ext_modules=[
          cpp_extension.CUDAExtension(
              'alpa.cpp_extension.calc_precision',
              ['alpa/cpp_extension/calc_precision.cc']
          ),
          cpp_extension.CUDAExtension(
              'alpa.cpp_extension.minimax',
              ['alpa/cpp_extension/minimax.cc', 'alpa/cpp_extension/minimax_cuda_kernel.cu']
          ),
          cpp_extension.CUDAExtension(
              'alpa.cpp_extension.quantization',
              ['alpa/cpp_extension/quantization.cc',
                  'alpa/cpp_extension/quantization_cuda_kernel.cu']
          ),
      ],
      cmdclass={'build_ext': cpp_extension.BuildExtension},
      packages=find_packages()
      )
