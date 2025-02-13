from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class MissDistance:
    astronomical: float
    kilometers: float
    lunar: float
    miles: float

    def __post_init__(self):
        self.astronomical = float(self.astronomical)
        self.kilometers = float(self.kilometers)
        self.lunar = float(self.lunar)
        self.miles = float(self.lunar)


@dataclass
class RelativeVelocity:
    kilometers_per_hour: float
    kilometers_per_second: float
    miles_per_hour: float

    def __post_init__(self):
        self.kilometers_per_hour = float(self.kilometers_per_hour)
        self.kilometers_per_second = float(self.kilometers_per_second)
        self.miles_per_hour = float(self.miles_per_hour)


@dataclass
class CloseApproachDataItem:
    close_approach_date: date
    close_approach_date_full: datetime
    epoch_date_close_approach: int
    miss_distance: MissDistance
    orbiting_body: str
    relative_velocity: RelativeVelocity

    def __post_init__(self):
        self.close_approach_date = date.fromisoformat(self.close_approach_date)
        self.close_approach_date_full = datetime.strptime(
            self.close_approach_date_full, '%Y-%b-%d %H:%M'
        )
        self.miss_distance = MissDistance(**self.miss_distance)
        self.relative_velocity = RelativeVelocity(**self.relative_velocity)


@dataclass
class OrbitClass:
    orbit_class_description: str
    orbit_class_range: str
    orbit_class_type: str


@dataclass
class OrbitalData:
    aphelion_distance: float
    ascending_node_longitude: float = field(repr=False)
    data_arc_in_days: int = field(repr=False)
    eccentricity: float
    epoch_osculation: float = field(repr=False)
    equinox: str = field(repr=False)
    first_observation_date: date
    inclination: float = field(repr=False)
    jupiter_tisserand_invariant: float = field(repr=False)
    last_observation_date: date
    mean_anomaly: float = field(repr=False)
    mean_motion: float = field(repr=False)
    minimum_orbit_intersection: float = field(repr=False)
    observations_used: int
    orbit_class: OrbitClass
    orbit_determination_date: datetime
    orbit_id: int
    orbit_uncertainty: int = field(repr=False)
    orbital_period: float
    perihelion_argument: float = field(repr=False)
    perihelion_distance: float
    perihelion_time: float
    semi_major_axis: float = field(repr=False)

    def __post_init__(self):
        self.aphelion_distance = float(self.aphelion_distance)
        self.ascending_node_longitude = float(self.ascending_node_longitude)
        self.eccentricity = float(self.eccentricity)
        self.epoch_osculation = float(self.epoch_osculation)
        self.first_observation_date = date.fromisoformat(self.first_observation_date)
        self.inclination = float(self.inclination)
        self.jupiter_tisserand_invariant = float(self.jupiter_tisserand_invariant)
        self.last_observation_date = date.fromisoformat(self.last_observation_date)
        self.mean_anomaly = float(self.mean_anomaly)
        self.mean_motion = float(self.mean_motion)
        self.minimum_orbit_intersection = float(self.minimum_orbit_intersection)
        self.orbit_class = OrbitClass(**self.orbit_class)
        self.orbit_determination_date = datetime.strptime(
            self.orbit_determination_date, '%Y-%m-%d %H:%M:%S'
        )
        self.orbit_id = int(self.orbit_id)
        self.orbit_uncertainty = int(self.orbit_uncertainty)
        self.orbital_period = float(self.orbital_period)
        self.perihelion_argument = float(self.perihelion_argument)
        self.perihelion_distance = float(self.perihelion_distance)
        self.perihelion_time = float(self.perihelion_time)
        self.semi_major_axis = float(self.semi_major_axis)


@dataclass
class NeoWs:
    absolute_magnitude_h: float = field(repr=False)
    close_approach_data: list[CloseApproachDataItem] = field(repr=False)
    estimated_diameter: dict = field(repr=False)
    id: int
    is_potentially_hazardous_asteroid: bool
    is_sentry_object: bool = field(repr=False)
    links: dict = field(repr=False)
    name: str
    nasa_jpl_url: str = field(repr=False)
    neo_reference_id: int
    designation: Optional[str] = field(repr=False, default=None)
    orbital_data: Optional[OrbitalData] = field(default=None)

    def __post_init__(self):
        self.id = int(self.id)
        self.neo_reference_id = int(self.neo_reference_id)
        if self.orbital_data is not None:
            self.orbital_data = OrbitalData(**self.orbital_data)
        self.close_approach_data = [
            CloseApproachDataItem(**item) for item in self.close_approach_data
        ]
