# (C) British Crown Copyright 2010 - 2013, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
#
# DO NOT EDIT: AUTO-GENERATED

import collections


CFName = collections.namedtuple('CFName', 'standard_name long_name units')


LBFC_TO_CF = {
    5: CFName('atmosphere_boundary_layer_thickness', None, 'm'),
    23: CFName('soil_temperature', None, 'K'),
    27: CFName('air_density', None, 'kg m-3'),
    36: CFName('land_area_fraction', None, '1'),
    37: CFName('sea_ice_area_fraction', None, '1'),
    50: CFName('wind_speed', None, 'm s-1'),
    73: CFName('atmosphere_relative_vorticity', None, 's-1'),
    74: CFName('divergence_of_wind', None, 's-1'),
    83: CFName('potential_vorticity_of_atmosphere_layer', None, 'Pa-1 s-1'),
    94: CFName('convective_rainfall_amount', None, 'kg m-2'),
    97: CFName('rainfall_flux', None, 'kg m-2 s-1'),
    102: CFName('stratiform_rainfall_amount', None, 'kg m-2'),
    108: CFName('snowfall_flux', None, 'kg m-2 s-1'),
    111: CFName('surface_runoff_amount', None, 'kg m-2'),
    116: CFName('stratiform_snowfall_amount', None, 'kg m-2'),
    117: CFName('convective_snowfall_amount', None, 'kg m-2'),
    122: CFName('moisture_content_of_soil_layer', None, 'kg m-2'),
    183: CFName('wind_speed', None, 'm s-1'),
    200: CFName('toa_incoming_shortwave_flux', None, 'W m-2'),
    203: CFName('surface_downwelling_shortwave_flux_in_air', None, 'W m-2'),
    206: CFName('toa_outgoing_longwave_flux', None, 'W m-2'),
    208: CFName('surface_downwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'),
    209: CFName('sea_ice_temperature', None, 'K'),
    253: CFName('tendency_of_air_temperature_due_to_longwave_heating', None, 'K s-1'),
    261: CFName('downward_heat_flux_in_sea_ice', None, 'W m-2'),
    321: CFName('root_depth', None, 'm'),
    326: CFName('vegetation_area_fraction', None, '1'),
    328: CFName('surface_albedo_assuming_deep_snow', None, '1'),
    329: CFName('volume_fraction_of_condensed_water_in_soil_at_wilting_point', None, '1'),
    330: CFName('volume_fraction_of_condensed_water_in_soil_at_critical_point', None, '1'),
    332: CFName('soil_porosity', None, '1'),
    333: CFName('soil_hydraulic_conductivity_at_saturation', None, 'm s-1'),
    335: CFName('soil_thermal_capacity', None, 'J kg-1 K-1'),
    336: CFName('soil_thermal_conductivity', None, 'W m-1 K-1'),
    342: CFName('soil_suction_at_saturation', None, 'Pa'),
    687: CFName('sea_ice_thickness', None, 'm'),
    701: CFName('surface_eastward_sea_water_velocity', None, 'm s-1'),
    702: CFName('surface_northward_sea_water_velocity', None, 'm s-1'),
    981: CFName('air_temperature', None, 'K'),
    982: CFName('specific_humidity', None, '1'),
    984: CFName('mass_fraction_of_cloud_ice_in_air', None, '1'),
    1025: CFName('surface_downward_eastward_stress', None, 'Pa'),
    1026: CFName('surface_downward_northward_stress', None, 'Pa'),
    1373: CFName('mass_fraction_of_dimethyl_sulfide_in_air', None, '1'),
    1374: CFName('mass_fraction_of_sulfur_dioxide_in_air', None, '1'),
    1382: CFName('leaf_area_index', None, '1'),
    1383: CFName('canopy_height', None, 'm'),
    1385: CFName('mass_fraction_of_unfrozen_water_in_soil_moisture', None, '1'),
    1386: CFName('mass_fraction_of_frozen_water_in_soil_moisture', None, '1'),
    1392: CFName('leaf_area_index', None, '1'),
    1393: CFName('canopy_height', None, 'm'),
    1395: CFName('soil_albedo', None, '1'),
    1507: CFName('snow_grain_size', None, '1e-6 m'),
    1559: CFName('soil_moisture_content_at_field_capacity', None, 'kg m-2'),
    1720: CFName('cloud_area_fraction_in_atmosphere_layer', None, '1'),
    }

STASH_TO_CF = {
    'm01s00i004': CFName('air_potential_temperature', None, 'K'),
    'm01s00i009': CFName('moisture_content_of_soil_layer', None, 'kg m-2'),
    'm01s00i010': CFName('specific_humidity', None, '1'),
    'm01s00i012': CFName('mass_fraction_of_cloud_ice_in_air', None, '1'),
    'm01s00i013': CFName('convective_cloud_area_fraction', None, '1'),
    'm01s00i020': CFName('soil_temperature', None, 'K'),
    'm01s00i023': CFName('snowfall_amount', None, 'kg m-2'),
    'm01s00i024': CFName('surface_temperature', None, 'K'),
    'm01s00i025': CFName('atmosphere_boundary_layer_thickness', None, 'm'),
    'm01s00i026': CFName('surface_roughness_length', None, 'm'),
    'm01s00i028': CFName('surface_eastward_sea_water_velocity', None, 'm s-1'),
    'm01s00i029': CFName('surface_northward_sea_water_velocity', None, 'm s-1'),
    'm01s00i030': CFName('land_binary_mask', None, '1'),
    'm01s00i031': CFName('sea_ice_area_fraction', None, '1'),
    'm01s00i032': CFName('sea_ice_thickness', None, 'm'),
    'm01s00i033': CFName('surface_altitude', None, 'm'),
    'm01s00i040': CFName('volume_fraction_of_condensed_water_in_soil_at_wilting_point', None, '1'),
    'm01s00i041': CFName('volume_fraction_of_condensed_water_in_soil_at_critical_point', None, '1'),
    'm01s00i043': CFName('soil_porosity', None, '1'),
    'm01s00i044': CFName('soil_hydraulic_conductivity_at_saturation', None, 'm s-1'),
    'm01s00i046': CFName('soil_thermal_capacity', None, 'J kg-1 K-1'),
    'm01s00i047': CFName('soil_thermal_conductivity', None, 'W m-1 K-1'),
    'm01s00i048': CFName('soil_suction_at_saturation', None, 'Pa'),
    'm01s00i049': CFName('sea_ice_temperature', None, 'K'),
    'm01s00i050': CFName('vegetation_area_fraction', None, '1'),
    'm01s00i051': CFName('root_depth', None, 'm'),
    'm01s00i052': CFName('surface_albedo_assuming_no_snow', None, '1'),
    'm01s00i053': CFName('surface_albedo_assuming_deep_snow', None, '1'),
    'm01s00i060': CFName('mass_fraction_of_ozone_in_air', None, '1'),
    'm01s00i101': CFName('mass_fraction_of_sulfur_dioxide_in_air', None, '1'),
    'm01s00i102': CFName('mass_fraction_of_dimethyl_sulfide_in_air', None, '1'),
    'm01s00i150': CFName('upward_air_velocity', None, 'm s-1'),
    'm01s00i205': CFName('land_area_fraction', None, '1'),
    'm01s00i208': CFName('leaf_area_index', None, '1'),
    'm01s00i209': CFName('canopy_height', None, 'm'),
    'm01s00i214': CFName('mass_fraction_of_unfrozen_water_in_soil_moisture', None, '1'),
    'm01s00i215': CFName('mass_fraction_of_frozen_water_in_soil_moisture', None, '1'),
    'm01s00i217': CFName('leaf_area_index', None, '1'),
    'm01s00i218': CFName('canopy_height', None, 'm'),
    'm01s00i220': CFName('soil_albedo', None, '1'),
    'm01s00i223': CFName('soil_carbon_content', None, 'kg m-2'),
    'm01s00i231': CFName('snow_grain_size', None, '1e-6 m'),
    'm01s00i252': CFName('mass_fraction_of_carbon_dioxide_in_air', None, '1'),
    'm01s00i254': CFName('mass_fraction_of_cloud_liquid_water_in_air', None, '1'),
    'm01s00i255': CFName('dimensionless_exner_function', None, '1'),
    'm01s00i269': CFName('surface_eastward_sea_water_velocity', None, 'm s-1'),
    'm01s00i270': CFName('surface_northward_sea_water_velocity', None, 'm s-1'),
    'm01s00i406': CFName('dimensionless_exner_function', None, '1'),
    'm01s00i407': CFName('air_pressure', None, 'Pa'),
    'm01s00i408': CFName('air_pressure', None, 'Pa'),
    'm01s00i409': CFName('surface_air_pressure', None, 'Pa'),
    'm01s00i505': CFName('land_area_fraction', None, '1'),
    'm01s00i506': CFName('surface_temperature', None, 'K'),
    'm01s00i507': CFName('surface_temperature', None, 'K'),
    'm01s00i508': CFName('surface_temperature', None, 'K'),
    'm01s00i509': CFName('sea_ice_albedo', None, '1'),
    'm01s01i004': CFName('air_temperature', None, 'K'),
    'm01s01i201': CFName('surface_net_downward_shortwave_flux', None, 'W m-2'),
    'm01s01i203': CFName('surface_net_downward_shortwave_flux', None, 'W m-2'),
    'm01s01i205': CFName('toa_outgoing_shortwave_flux', None, 'W m-2'),
    'm01s01i207': CFName('toa_incoming_shortwave_flux', None, 'W m-2'),
    'm01s01i209': CFName('toa_outgoing_shortwave_flux_assuming_clear_sky', None, 'W m-2'),
    'm01s01i210': CFName('surface_downwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'),
    'm01s01i211': CFName('surface_upwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'),
    'm01s01i235': CFName('surface_downwelling_shortwave_flux_in_air', None, 'W m-2'),
    'm01s01i410': CFName('surface_downwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'),
    'm01s01i435': CFName('surface_downwelling_shortwave_flux_in_air', None, 'W m-2'),
    'm01s02i004': CFName('air_temperature', None, 'K'),
    'm01s02i201': CFName('surface_net_downward_longwave_flux', None, 'W m-2'),
    'm01s02i203': CFName('surface_net_downward_longwave_flux', None, 'W m-2'),
    'm01s02i204': CFName('cloud_area_fraction', None, '1'),
    'm01s02i205': CFName('toa_outgoing_longwave_flux', None, 'W m-2'),
    'm01s02i206': CFName('toa_outgoing_longwave_flux_assuming_clear_sky', None, 'W m-2'),
    'm01s02i232': CFName('tendency_of_air_temperature_due_to_longwave_heating', None, 'K s-1'),
    'm01s02i260': CFName('mass_fraction_of_ozone_in_air', None, '1'),
    'm01s02i261': CFName('cloud_area_fraction_in_atmosphere_layer', None, '1'),
    'm01s03i004': CFName('air_temperature', None, 'm s-1'),
    'm01s03i010': CFName('specific_humidity', None, '1'),
    'm01s03i025': CFName('atmosphere_boundary_layer_thickness', None, 'm'),
    'm01s03i201': CFName('downward_heat_flux_in_sea_ice', None, 'W m-2'),
    'm01s03i217': CFName('surface_upward_sensible_heat_flux', None, 'W m-2'),
    'm01s03i223': CFName('surface_upward_water_flux', None, 'kg m-2 s-1'),
    'm01s03i224': CFName('wind_mixing_energy_flux_into_sea_water', None, 'W m-2'),
    'm01s03i227': CFName('wind_speed', None, 'm s-1'),
    'm01s03i228': CFName('surface_upward_sensible_heat_flux', None, 'W m-2'),
    'm01s03i230': CFName('wind_speed', None, 'm s-1'),
    'm01s03i236': CFName('air_temperature', None, 'K'),
    'm01s03i238': CFName('soil_temperature', None, 'K'),
    'm01s03i245': CFName('relative_humidity', None, '%'),
    'm01s03i250': CFName('dew_point_temperature', None, 'K'),
    'm01s03i313': CFName('soil_moisture_content_at_field_capacity', None, 'kg m-2'),
    'm01s03i332': CFName('toa_outgoing_longwave_flux', None, 'W m-2'),
    'm01s03i334': CFName('water_potential_evaporation_flux', None, 'kg m-2 s-1'),
    'm01s03i337': CFName('downward_heat_flux_in_soil', None, 'W m-2'),
    'm01s03i391': CFName('surface_downward_eastward_stress', None, 'Pa'),
    'm01s03i392': CFName('surface_downward_eastward_stress', None, 'Pa'),
    'm01s03i393': CFName('surface_downward_northward_stress', None, 'Pa'),
    'm01s03i394': CFName('surface_downward_northward_stress', None, 'Pa'),
    'm01s03i460': CFName('surface_downward_eastward_stress', None, 'Pa'),
    'm01s03i461': CFName('surface_downward_northward_stress', None, 'Pa'),
    'm01s04i004': CFName('air_temperature', None, 'K'),
    'm01s04i010': CFName('specific_humidity', None, '1'),
    'm01s04i201': CFName('stratiform_rainfall_amount', None, 'kg m-2'),
    'm01s04i202': CFName('stratiform_snowfall_amount', None, 'kg m-2'),
    'm01s04i203': CFName('stratiform_rainfall_rate', None, 'kg m-2 s-1'),
    'm01s04i204': CFName('stratiform_snowfall_rate', None, 'kg m-2 s-1'),
    'm01s05i010': CFName('specific_humidity', None, '1'),
    'm01s05i181': CFName('tendency_of_air_temperature_due_to_convection', None, 'K s-1'),
    'm01s05i182': CFName('tendency_of_specific_humidity_due_to_convection', None, 's-1'),
    'm01s05i185': CFName('tendency_of_eastward_wind_due_to_convection', None, 'm s-2'),
    'm01s05i186': CFName('tendency_of_northward_wind_due_to_convection', None, 'm s-2'),
    'm01s05i201': CFName('convective_rainfall_amount', None, 'kg m-2'),
    'm01s05i202': CFName('convective_snowfall_amount', None, 'kg m-2'),
    'm01s05i209': CFName('air_temperature', None, 'K'),
    'm01s05i214': CFName('rainfall_flux', None, 'kg m-2 s-1'),
    'm01s05i215': CFName('snowfall_flux', None, 'kg m-2 s-1'),
    'm01s06i185': CFName('tendency_of_eastward_wind_due_to_gravity_wave_drag', None, 'm s-2'),
    'm01s06i186': CFName('tendency_of_northward_wind_due_to_gravity_wave_drag', None, 'm s-2'),
    'm01s06i201': CFName('atmosphere_eastward_stress_due_to_gravity_wave_drag', None, 'Pa'),
    'm01s06i202': CFName('atmosphere_northward_stress_due_to_gravity_wave_drag', None, 'Pa'),
    'm01s08i023': CFName('surface_snow_amount', None, 'kg m-2'),
    'm01s08i204': CFName('surface_runoff_amount', None, 'kg m-2'),
    'm01s08i205': CFName('subsurface_runoff_amount', None, 'kg m-2'),
    'm01s08i223': CFName('moisture_content_of_soil_layer', None, 'kg m-2'),
    'm01s08i225': CFName('soil_temperature', None, 'K'),
    'm01s08i234': CFName('surface_runoff_flux', None, 'kg m-2 s-1'),
    'm01s08i235': CFName('subsurface_runoff_flux', None, 'kg m-2 s-1'),
    'm01s09i004': CFName('air_temperature', None, 'K'),
    'm01s09i010': CFName('specific_humidity', None, '1'),
    'm01s09i201': CFName('stratiform_cloud_area_fraction_in_atmosphere_layer', None, '1'),
    'm01s12i004': CFName('air_temperature', None, 'K'),
    'm01s12i010': CFName('specific_humidity', None, '1'),
    'm01s12i012': CFName('mass_fraction_of_cloud_ice_in_air', None, '1'),
    'm01s12i181': CFName('tendency_of_air_temperature_due_to_advection', None, 'K s-1'),
    'm01s12i182': CFName('tendency_of_specific_humidity_due_to_advection', None, 's-1'),
    'm01s12i183': CFName('tendency_of_mass_fraction_of_cloud_liquid_water_in_air_due_to_advection', None, 's-1'),
    'm01s12i184': CFName('tendency_of_mass_fraction_of_cloud_ice_in_air_due_to_advection', None, 's-1'),
    'm01s12i185': CFName('tendency_of_eastward_wind_due_to_advection', None, 'm s-1'),
    'm01s12i186': CFName('tendency_of_northward_wind_due_to_advection', None, 'm s-1'),
    'm01s12i187': CFName('tendency_of_upward_air_velocity_due_to_advection', None, 'm s-1'),
    'm01s13i181': CFName('tendency_of_air_temperature_due_to_diffusion', None, 'K s-1'),
    'm01s13i182': CFName('tendency_of_specific_humidity_due_to_diffusion', None, 's-1'),
    'm01s13i185': CFName('tendency_of_eastward_wind_due_to_diffusion', None, 'm s-1'),
    'm01s13i186': CFName('tendency_of_northward_wind_due_to_diffusion', None, 'm s-1'),
    'm01s15i108': CFName('air_pressure', None, 'Pa'),
    'm01s15i119': CFName('air_potential_temperature', None, 'K'),
    'm01s15i127': CFName('air_density', None, 'kg m-3'),
    'm01s15i142': CFName('upward_air_velocity', None, 'm s-1'),
    'm01s15i143': CFName('eastward_wind', None, 'm s-1'),
    'm01s15i144': CFName('northward_wind', None, 'm s-1'),
    'm01s15i201': CFName('eastward_wind', None, 'm s-1'),
    'm01s15i202': CFName('northward_wind', None, 'm s-1'),
    'm01s15i214': CFName('ertel_potential_vorticity', None, 'K m2 kg-1 s-1'),
    'm01s15i215': CFName('air_potential_temperature', None, 'K'),
    'm01s15i216': CFName('air_potential_temperature', None, 'K'),
    'm01s15i217': CFName('potential_vorticity_of_atmosphere_layer', None, 'Pa-1 s-1'),
    'm01s15i218': CFName('potential_vorticity_of_atmosphere_layer', None, 'Pa-1 s-1'),
    'm01s15i242': CFName('upward_air_velocity', None, 'm s-1'),
    'm01s15i243': CFName('eastward_wind', None, 'm s-1'),
    'm01s15i244': CFName('northward_wind', None, 'm s-1'),
    'm01s16i004': CFName('air_temperature', None, 'K'),
    'm01s16i201': CFName('geopotential_height', None, 'm'),
    'm01s16i202': CFName('geopotential_height', None, 'm'),
    'm01s16i203': CFName('air_temperature', None, 'K'),
    'm01s16i222': CFName('air_pressure_at_sea_level', None, 'Pa'),
    'm01s16i255': CFName('geopotential_height', None, 'm'),
    'm01s20i003': CFName('wind_speed', None, 'm s-1'),
    'm01s20i004': CFName('wind_speed', None, 'm s-1'),
    'm01s20i005': CFName('divergence_of_wind', None, 's-1'),
    'm01s20i006': CFName('atmosphere_relative_vorticity', None, 's-1'),
    'm01s20i024': CFName('tropopause_air_pressure', None, 'Pa'),
    'm01s20i025': CFName('tropopause_air_temperature', None, 'K'),
    'm01s20i026': CFName('tropopause_altitude', None, 'm'),
    'm01s20i034': CFName('air_pressure_at_freezing_level', None, 'Pa'),
    'm01s20i064': CFName('tropopause_air_pressure', None, 'Pa'),
    'm01s20i065': CFName('tropopause_air_temperature', None, 'K'),
    'm01s20i066': CFName('tropopause_altitude', None, 'm'),
    'm01s30i003': CFName('upward_air_velocity', None, 'm s-1'),
    'm01s30i004': CFName('air_temperature', None, 'K'),
    'm01s30i005': CFName('specific_humidity', None, '1'),
    'm01s30i007': CFName('specific_kinetic_energy_of_air', None, 'm2 s-2'),
    'm01s30i111': CFName('air_temperature', None, 'K'),
    'm01s30i113': CFName('relative_humidity', None, '%'),
    'm01s30i181': CFName('tendency_of_air_temperature', None, 'K s-1'),
    'm01s30i182': CFName('tendency_of_specific_humidity', None, 's-1'),
    'm01s30i183': CFName('tendency_of_mass_fraction_of_cloud_liquid_water_in_air', None, 's-1'),
    'm01s30i184': CFName('tendency_of_mass_fraction_of_cloud_ice_in_air', None, 's-1'),
    'm01s30i185': CFName('tendency_of_eastward_wind', None, 'm s-1'),
    'm01s30i186': CFName('tendency_of_northward_wind', None, 'm s-1'),
    'm01s30i187': CFName('tendency_of_upward_air_velocity', None, 'm s-1'),
    'm01s30i188': CFName('tendency_of_air_density', None, 'kg m-3 s-1'),
    'm01s30i201': CFName('eastward_wind', None, 'm s-1'),
    'm01s30i202': CFName('northward_wind', None, 'm s-1'),
    'm01s30i203': CFName('upward_air_velocity', None, 'm s-1'),
    'm01s30i204': CFName('air_temperature', None, 'K'),
    'm01s30i205': CFName('specific_humidity', None, '1'),
    'm01s30i207': CFName('geopotential_height', None, 'm'),
    'm01s30i208': CFName('lagrangian_tendency_of_air_pressure', None, 'Pa s-1'),
    'm01s30i211': CFName('square_of_eastward_wind', None, 'm2 s-2'),
    'm01s30i212': CFName('product_of_eastward_wind_and_northward_wind', None, 'm2 s-2'),
    'm01s30i213': CFName('product_of_eastward_wind_and_upward_air_velocity', None, 'm2 s-2'),
    'm01s30i214': CFName('product_of_eastward_wind_and_air_temperature', None, 'K m s-1'),
    'm01s30i215': CFName('product_of_eastward_wind_and_specific_humidity', None, 'm s-1'),
    'm01s30i217': CFName('product_of_eastward_wind_and_geopotential_height', None, 'm2 s-1'),
    'm01s30i218': CFName('product_of_eastward_wind_and_omega', None, 'Pa m s-1'),
    'm01s30i222': CFName('square_of_northward_wind', None, 'm2 s-2'),
    'm01s30i223': CFName('product_of_northward_wind_and_upward_air_velocity', None, 'm2 s-2'),
    'm01s30i224': CFName('product_of_northward_wind_and_air_temperature', None, 'K m s-1'),
    'm01s30i225': CFName('product_of_northward_wind_and_specific_humidity', None, 'm s-1'),
    'm01s30i227': CFName('product_of_northward_wind_and_geopotential_height', None, 'm2 s-1'),
    'm01s30i228': CFName('product_of_northward_wind_and_omega', None, 'Pa m s-1'),
    'm01s30i233': CFName('square_of_upward_air_velocity', None, 'm2 s-2'),
    'm01s30i234': CFName('product_of_upward_air_velocity_and_air_temperature', None, 'K m s-1'),
    'm01s30i235': CFName('product_of_upward_air_velocity_and_specific_humidity', None, 'm s-1'),
    'm01s30i244': CFName('square_of_air_temperature', None, 'K2'),
    'm01s30i245': CFName('product_of_air_temperature_and_specific_humidity', None, 'K'),
    'm01s30i248': CFName('product_of_air_temperature_and_omega', None, 'K Pa s-1'),
    'm01s30i258': CFName('product_of_specific_humidity_and_omega', None, 'Pa s-1'),
    'm01s30i277': CFName('square_of_geopotential_height', None, 'm2'),
    'm01s30i278': CFName('product_of_geopotential_height_and_omega', None, 'Pa m s-1'),
    'm01s30i288': CFName('square_of_lagrangian_tendency_of_air_pressure', None, 'Pa2 s-2'),
    'm01s30i302': CFName('virtual_temperature', None, 'K'),
    'm01s30i401': CFName('atmosphere_kinetic_energy_content', None, 'J m-2'),
    'm01s30i405': CFName('atmosphere_cloud_liquid_water_content', None, 'kg m-2'),
    'm01s30i406': CFName('atmosphere_cloud_ice_content', None, 'kg m-2'),
    'm01s30i417': CFName('surface_air_pressure', None, 'Pa'),
    'm01s30i418': CFName('surface_air_pressure', None, 'Pa'),
    'm01s30i451': CFName('tropopause_air_pressure', None, 'Pa'),
    'm01s30i452': CFName('tropopause_air_temperature', None, 'K'),
    'm01s30i453': CFName('tropopause_altitude', None, 'm'),
    'm01s33i041': CFName('mole_fraction_of_atomic_chlorine_in_air', None, '1'),
    'm01s33i042': CFName('mole_fraction_of_chlorine_monoxide_in_air', None, '1'),
    'm01s33i043': CFName('mole_fraction_of_dichlorine_peroxide_in_air', None, '1'),
    'm01s33i044': CFName('mole_fraction_of_chlorine_dioxide_in_air', None, '1'),
    'm01s33i047': CFName('mole_fraction_of_bromine_chloride_in_air', None, '1'),
    'm01s33i048': CFName('mole_fraction_of_bromine_nitrate_in_air', None, '1'),
    'm01s33i049': CFName('mole_fraction_of_nitrous_oxide_in_air', None, '1'),
    'm01s33i051': CFName('mole_fraction_of_hypochlorous_acid_in_air', None, '1'),
    'm01s33i054': CFName('mole_fraction_of_chlorine_nitrate_in_air', None, '1'),
    'm01s33i055': CFName('mole_fraction_of_cfc11_in_air', None, '1'),
    'm01s33i056': CFName('mole_fraction_of_cfc12_in_air', None, '1'),
    'm01s33i058': CFName('mole_fraction_of_atomic_nitrogen_in_air', None, '1'),
    'm01s33i150': CFName('age_of_stratospheric_air', None, '1'),
    'm02s00i101': CFName('sea_water_potential_temperature', None, 'degC'),
    'm02s00i102': CFName('sea_water_salinity', None, '1e3 psu @0.035'),
    'm02s00i121': CFName('baroclinic_eastward_sea_water_velocity', None, 'cm s-1'),
    'm02s00i122': CFName('baroclinic_northward_sea_water_velocity', None, 'cm s-1'),
    'm02s00i130': CFName('ocean_barotropic_streamfunction', None, 'cm3 s-1'),
    'm02s00i131': CFName('ocean_barotropic_streamfunction', None, 'cm3 s-1'),
    'm02s00i132': CFName('tendency_of_ocean_barotropic_streamfunction', None, 'cm3 s-2'),
    'm02s00i133': CFName('tendency_of_ocean_barotropic_streamfunction', None, 'cm3 s-2'),
    'm02s00i134': CFName('surface_air_pressure', None, 'g cm-1 s-2'),
    'm02s00i135': CFName('barotropic_eastward_sea_water_velocity', None, 'cm s-1'),
    'm02s00i136': CFName('barotropic_northward_sea_water_velocity', None, 'cm s-1'),
    'm02s00i137': CFName('ocean_mixed_layer_thickness', None, 'm'),
    'm02s00i139': CFName('downward_eastward_stress_at_sea_ice_base', None, 'Pa'),
    'm02s00i140': CFName('downward_northward_stress_at_sea_ice_base', None, 'Pa'),
    'm02s00i141': CFName('surface_snow_thickness', None, 'm'),
    'm02s00i143': CFName('upward_sea_ice_basal_heat_flux', None, 'W m-2'),
    'm02s00i146': CFName('sea_ice_area_fraction', None, '1'),
    'm02s00i147': CFName('sea_ice_thickness', None, 'm'),
    'm02s00i148': CFName('eastward_sea_ice_velocity', None, 'm s-1'),
    'm02s00i149': CFName('northward_sea_ice_velocity', None, 'm s-1'),
    'm02s00i150': CFName('surface_downward_eastward_stress', None, 'Pa'),
    'm02s00i151': CFName('surface_downward_northward_stress', None, 'Pa'),
    'm02s00i152': CFName('wind_mixing_energy_flux_into_sea_water', None, 'W m-2'),
    'm02s00i166': CFName('water_flux_into_sea_water_from_rivers', None, 'kg m-2 s-1'),
    'm02s00i171': CFName('snowfall_flux', None, 'kg m-2 s-1'),
    'm02s00i180': CFName('sea_surface_temperature', None, 'K'),
    'm02s00i181': CFName('sea_surface_salinity', None, '1e3 psu @0.035'),
    'm02s00i182': CFName('air_temperature', None, 'K'),
    'm02s00i183': CFName('sea_ice_thickness', None, 'm'),
    'm02s00i185': CFName('heat_flux_correction', None, 'W m-2'),
    'm02s00i186': CFName('water_flux_correction', None, 'Kg m-2 s-1'),
    'm02s00i190': CFName('surface_snow_and_ice_melt_heat_flux', None, 'W m-2'),
    'm02s00i191': CFName('downward_heat_flux_in_sea_ice', None, 'W m-2'),
    'm02s30i201': CFName('upward_sea_water_velocity', None, 'cm s-1'),
    'm02s30i202': CFName('ocean_mixed_layer_thickness', None, 'm'),
    'm02s30i211': CFName('northward_ocean_heat_transport', None, 'PW'),
    'm02s30i212': CFName('northward_ocean_salt_transport', None, '1e7kg s-1'),
    'm02s30i320': CFName('eastward_sea_water_velocity', None, 'cm s-1'),
    'm02s30i321': CFName('northward_sea_water_velocity', None, 'cm s-1'),
    'm02s30i324': CFName('ocean_mixed_layer_thickness', None, 'm'),
    'm02s32i201': CFName('tendency_of_sea_ice_area_fraction_due_to_dynamics', None, 's-1'),
    'm02s32i202': CFName('tendency_of_sea_ice_thickness_due_to_dynamics', None, 'm s-1'),
    'm02s32i209': CFName('eastward_sea_ice_velocity', None, 'm s-1'),
    'm02s32i210': CFName('northward_sea_ice_velocity', None, 'm s-1'),
    'm02s32i211': CFName('tendency_of_sea_ice_area_fraction_due_to_thermodynamics', None, 's-1'),
    'm02s32i212': CFName('tendency_of_sea_ice_thickness_due_to_thermodynamics', None, 'm s-1'),
    'm02s32i219': CFName('downward_eastward_stress_at_sea_ice_base', None, 'Pa'),
    'm02s32i220': CFName('downward_northward_stress_at_sea_ice_base', None, 'Pa'),
    'm01s16i256': CFName('relative_humidity', None, '%'),
    }

CF_TO_LBFC = {
    CFName('age_of_stratospheric_air', None, '1'): 501,
    CFName('air_density', None, 'kg m-3'): 27,
    CFName('air_potential_temperature', None, 'K'): 19,
    CFName('air_pressure', None, 'Pa'): 8,
    CFName('air_pressure_at_freezing_level', None, 'Pa'): 8,
    CFName('air_pressure_at_sea_level', None, 'Pa'): 8,
    CFName('atmosphere_boundary_layer_thickness', None, 'm'): 5,
    CFName('atmosphere_eastward_stress_due_to_gravity_wave_drag', None, 'Pa'): 61,
    CFName('atmosphere_kinetic_energy_content', None, 'J m-2'): 63,
    CFName('atmosphere_northward_stress_due_to_gravity_wave_drag', None, 'Pa'): 62,
    CFName('atmosphere_relative_vorticity', None, 's-1'): 73,
    CFName('cloud_area_fraction', None, '1'): 30,
    CFName('cloud_area_fraction_in_atmosphere_layer', None, '1'): 1720,
    CFName('convective_cloud_area_fraction', None, '1'): 34,
    CFName('convective_rainfall_amount', None, 'kg m-2'): 94,
    CFName('convective_snowfall_amount', None, 'kg m-2'): 117,
    CFName('dimensionless_exner_function', None, '1'): 7,
    CFName('divergence_of_wind', None, 's-1'): 74,
    CFName('downward_heat_flux_in_sea_ice', None, 'W m-2'): 261,
    CFName('downward_heat_flux_in_soil', None, 'W m-2'): 1564,
    CFName('ertel_potential_vorticity', None, 'K m2 kg-1 s-1'): 82,
    CFName('geopotential_height', None, 'm'): 1,
    CFName('lagrangian_tendency_of_air_pressure', None, 'Pa s-1'): 40,
    CFName('land_binary_mask', None, '1'): 395,
    CFName('mass_fraction_of_carbon_dioxide_in_air', None, '1'): 1564,
    CFName('mass_fraction_of_cloud_liquid_water_in_air', None, '1'): 79,
    CFName('mass_fraction_of_dimethyl_sulfide_in_air', None, '1'): 1373,
    CFName('mass_fraction_of_frozen_water_in_soil_moisture', None, '1'): 1386,
    CFName('mass_fraction_of_ozone_in_air', None, '1'): 453,
    CFName('mass_fraction_of_sulfur_dioxide_in_air', None, '1'): 1374,
    CFName('mass_fraction_of_unfrozen_water_in_soil_moisture', None, '1'): 1385,
    CFName('moisture_content_of_soil_layer', None, 'kg m-2'): 122,
    CFName('mole_fraction_of_atomic_chlorine_in_air', None, '1'): 501,
    CFName('mole_fraction_of_atomic_nitrogen_in_air', None, '1'): 501,
    CFName('mole_fraction_of_bromine_chloride_in_air', None, '1'): 501,
    CFName('mole_fraction_of_bromine_nitrate_in_air', None, '1'): 501,
    CFName('mole_fraction_of_cfc11_in_air', None, '1'): 501,
    CFName('mole_fraction_of_cfc12_in_air', None, '1'): 501,
    CFName('mole_fraction_of_chlorine_dioxide_in_air', None, '1'): 501,
    CFName('mole_fraction_of_chlorine_monoxide_in_air', None, '1'): 501,
    CFName('mole_fraction_of_chlorine_nitrate_in_air', None, '1'): 501,
    CFName('mole_fraction_of_dichlorine_peroxide_in_air', None, '1'): 501,
    CFName('mole_fraction_of_hypochlorous_acid_in_air', None, '1'): 501,
    CFName('mole_fraction_of_nitrous_oxide_in_air', None, '1'): 501,
    CFName('rainfall_flux', None, 'kg m-2 s-1'): 97,
    CFName('relative_humidity', None, '%'): 88,
    CFName('root_depth', None, 'm'): 321,
    CFName('sea_ice_albedo', None, '1'): 322,
    CFName('sea_ice_area_fraction', None, '1'): 37,
    CFName('sea_ice_temperature', None, 'K'): 209,
    CFName('sea_ice_thickness', None, 'm'): 687,
    CFName('snow_grain_size', None, '1e-6 m'): 1507,
    CFName('snowfall_amount', None, 'kg m-2'): 93,
    CFName('snowfall_flux', None, 'kg m-2 s-1'): 108,
    CFName('soil_albedo', None, '1'): 1395,
    CFName('soil_carbon_content', None, 'kg m-2'): 1397,
    CFName('soil_hydraulic_conductivity_at_saturation', None, 'm s-1'): 333,
    CFName('soil_moisture_content_at_field_capacity', None, 'kg m-2'): 1559,
    CFName('soil_porosity', None, '1'): 332,
    CFName('soil_suction_at_saturation', None, 'Pa'): 342,
    CFName('soil_temperature', None, 'K'): 23,
    CFName('soil_thermal_capacity', None, 'J kg-1 K-1'): 335,
    CFName('soil_thermal_conductivity', None, 'W m-1 K-1'): 336,
    CFName('specific_kinetic_energy_of_air', None, 'm2 s-2'): 60,
    CFName('stratiform_cloud_area_fraction_in_atmosphere_layer', None, '1'): 220,
    CFName('stratiform_rainfall_amount', None, 'kg m-2'): 102,
    CFName('stratiform_rainfall_rate', None, 'kg m-2 s-1'): 99,
    CFName('stratiform_snowfall_amount', None, 'kg m-2'): 116,
    CFName('stratiform_snowfall_rate', None, 'kg m-2 s-1'): 118,
    CFName('subsurface_runoff_amount', None, 'kg m-2'): 112,
    CFName('subsurface_runoff_flux', None, 'kg m-2 s-1'): 1533,
    CFName('surface_albedo_assuming_deep_snow', None, '1'): 328,
    CFName('surface_albedo_assuming_no_snow', None, '1'): 322,
    CFName('surface_altitude', None, 'm'): 1,
    CFName('surface_downwelling_shortwave_flux_in_air', None, 'W m-2'): 203,
    CFName('surface_downwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'): 208,
    CFName('surface_eastward_sea_water_velocity', None, 'm s-1'): 701,
    CFName('surface_net_downward_longwave_flux', None, 'W m-2'): 187,
    CFName('surface_net_downward_shortwave_flux', None, 'W m-2'): 186,
    CFName('surface_northward_sea_water_velocity', None, 'm s-1'): 702,
    CFName('surface_roughness_length', None, 'm'): 324,
    CFName('surface_runoff_amount', None, 'kg m-2'): 111,
    CFName('surface_runoff_flux', None, 'kg m-2 s-1'): 1532,
    CFName('surface_snow_amount', None, 'kg m-2'): 93,
    CFName('surface_temperature', None, 'K'): 16,
    CFName('surface_upward_sensible_heat_flux', None, 'W m-2'): 178,
    CFName('surface_upward_water_flux', None, 'kg m-2 s-1'): 184,
    CFName('surface_upwelling_shortwave_flux_in_air_assuming_clear_sky', None, 'W m-2'): 207,
    CFName('tendency_of_air_density', None, 'kg m-3 s-1'): 7,
    CFName('tendency_of_air_temperature', None, 'K s-1'): 16,
    CFName('tendency_of_air_temperature_due_to_diffusion', None, 'K s-1'): 16,
    CFName('tendency_of_air_temperature_due_to_longwave_heating', None, 'K s-1'): 253,
    CFName('tendency_of_eastward_wind', None, 'm s-1'): 56,
    CFName('tendency_of_eastward_wind_due_to_diffusion', None, 'm s-1'): 56,
    CFName('tendency_of_mass_fraction_of_cloud_ice_in_air', None, 's-1'): 78,
    CFName('tendency_of_mass_fraction_of_cloud_liquid_water_in_air', None, 's-1'): 79,
    CFName('tendency_of_northward_wind', None, 'm s-1'): 57,
    CFName('tendency_of_northward_wind_due_to_diffusion', None, 'm s-1'): 57,
    CFName('tendency_of_specific_humidity', None, 's-1'): 95,
    CFName('tendency_of_specific_humidity_due_to_diffusion', None, 's-1'): 95,
    CFName('tendency_of_upward_air_velocity', None, 'm s-1'): 42,
    CFName('toa_incoming_shortwave_flux', None, 'W m-2'): 200,
    CFName('toa_outgoing_longwave_flux', None, 'W m-2'): 206,
    CFName('toa_outgoing_longwave_flux_assuming_clear_sky', None, 'W m-2'): 210,
    CFName('toa_outgoing_shortwave_flux', None, 'W m-2'): 201,
    CFName('toa_outgoing_shortwave_flux_assuming_clear_sky', None, 'W m-2'): 207,
    CFName('tropopause_air_pressure', None, 'Pa'): 8,
    CFName('tropopause_air_temperature', None, 'K'): 16,
    CFName('tropopause_altitude', None, 'm'): 1,
    CFName('upward_air_velocity', None, 'm s-1'): 42,
    CFName('vegetation_area_fraction', None, '1'): 326,
    CFName('virtual_temperature', None, 'K'): 16,
    CFName('volume_fraction_of_condensed_water_in_soil_at_critical_point', None, '1'): 330,
    CFName('volume_fraction_of_condensed_water_in_soil_at_wilting_point', None, '1'): 329,
    CFName('water_potential_evaporation_flux', None, 'kg m-2 s-1'): 115,
    CFName('wind_mixing_energy_flux_into_sea_water', None, 'W m-2'): 182,
    }
