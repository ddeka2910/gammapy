# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Built-in models in Gammapy."""
from .cube import *
from .spatial import *
from .spectral import *
from .spectral_cosmic_ray import *
from .spectral_crab import *
from .time import *

SPATIAL_MODELS = {
    "SkyDiffuseMap": SkyDiffuseMap,
    "SkyDisk": SkyDisk,
    "SkyEllipse": SkyEllipse,
    "SkyGaussian": SkyGaussian,
    "SkyGaussianElongated": SkyGaussianElongated,
    "SkyPointSource": SkyPointSource,
    "SkyShell": SkyShell,
}

TIME_MODELS = {
    "PhaseCurveTableModel": PhaseCurveTableModel,
    "LightCurveTableModel": LightCurveTableModel,
}

# TODO: add support for these models writing their .from_dict()
# "AbsorbedSpectralModel":AbsorbedSpectralModel,
# "Absorption":Absorption,
# "NaimaModel":NaimaModel,
SPECTRAL_MODELS = {
    "ConstantModel": ConstantModel,
    "PowerLaw": PowerLaw,
    "PowerLaw2": PowerLaw2,
    "ExponentialCutoffPowerLaw": ExponentialCutoffPowerLaw,
    "ExponentialCutoffPowerLaw3FGL": ExponentialCutoffPowerLaw3FGL,
    "PLSuperExpCutoff3FGL": PLSuperExpCutoff3FGL,
    "PLSuperExpCutoff4FGL": PLSuperExpCutoff4FGL,
    "LogParabola": LogParabola,
    "TableModel": TableModel,
    "SpectralGaussian": SpectralGaussian,
    "SpectralLogGaussian": SpectralLogGaussian,
    "ScaleModel": ScaleModel,
}