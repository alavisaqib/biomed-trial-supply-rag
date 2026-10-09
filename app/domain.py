import math
from .models import predict
from .config import SPEC

def transform(features):
    return [features[name] for name in SPEC['model_features']]

def result(action, summary, signals, steps):
    return {'minimum_action':action, 'summary':summary, 'signals':signals, 'next_steps':steps}

def analyze(f):
    forecast, residual=predict(f)
    baseline=f['enrollment_per_week']*f['kits_per_participant']
    lead=baseline*f['lead_time_days']/7
    reorder=math.ceil(baseline*(f['lead_time_days']+14)/7)
    needed=max(0,reorder-int(f['on_hand_kits']))
    action='escalate' if f['on_hand_kits']<lead or f['expiry_days']<=f['lead_time_days'] else 'review' if needed>0 else 'monitor'
    return result(action, f'Planning reorder point {reorder} kits; suggested replenishment {needed} kits.',
        {'forecast_kits_per_week':round(max(0,forecast),1),'baseline_kits_per_week':round(baseline,1),'reorder_point_kits':reorder,'suggested_kits':needed},
        ['Validate enrollment assumptions and lot-specific expiry.', 'Review suggested replenishment with the trial supply manager before ordering.'])

def simulate(rng):
    enrollment=rng.uniform(2,100); kits=int(rng.integers(1,7)); stock=int(rng.integers(0,1000)); lead=int(rng.integers(3,35)); expiry=int(rng.integers(5,180))
    target=max(0,float(rng.poisson(enrollment))*kits+rng.normal(0,3))
    return [enrollment,kits,stock,lead,expiry], target
