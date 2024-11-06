import socket

from diffuser.utils import watch

#------------------------ base ------------------------#

## automatically make experiment names for planning
## by labelling folders with these args

diffusion_args_to_watch = [
    ('prefix', ''),
    ('horizon', 'H'),
    ('n_diffusion_steps', 'T'),
]


plan_args_to_watch = [
    ('prefix', ''),
    ##
    ('horizon', 'H'),
    ('n_diffusion_steps', 'T'),
    ('value_horizon', 'V'),
    ('discount', 'd'),
    ('normalizer', ''),
    ('batch_size', 'b'),
    ##
    ('conditional', 'cond'),
]

base = {

    'diffusion': {
        ## model
        'model': 'models.ConditionalUnet1D',
        'diffusion': 'models.CFM',
        'horizon': 60,
        'global_cond_dim': 0,
        'n_diffusion_steps': 100,
        'action_weight': 1,
        'loss_weights': None,
        'loss_discount': 1,
        'predict_epsilon': False,
        'dim_mults': (1, 4, 8),
        'renderer': 'utils.PrisonerRendererGlobe',
        'num_past_obs': 10, 

        ## dataset
        'loader': 'datasets.SidotiAircraftSeparateLastN',
        'use_wavelet': False,
        # 'datapath': '/coc/data/prisoner_datasets/flight_data/N172CK/train',
        # 'test_datapath': '/coc/data/prisoner_datasets/flight_data/N172CK/test',
        'datapath': '/home/sean/FlightData/processed/N172CK/train',
        'test_datapath': '/home/sean/FlightData/processed/N172CK/test',

        # 'datapath': '/home/sean/FlightData/processed/N172CK/2018',
        # 'test_datapath': '/home/sean/FlightData/processed/N172CK/2019',

        # 'datapath': '/coc/data/prisoner_datasets/flight_data/N172CK/train',
        # 'test_datapath': '/coc/data/prisoner_datasets/flight_data/N172CK/test',

        'clip_denoised': True,
        'termination_penalty': None,
        'cont': None,

        ## serialization
        # 'logbase': '/coc/data/sye40/prisoner_logs/aircraft_sidoti_separate/cfm',
        # 'logbase': '/coc/data/sye40/prisoner_logs/IROS24/aircraft_sidoti_last_n',
        'logbase': '/home/sean/prisoner_logs/aircraft_sidoti_last_n_IROS24/',
        'prefix': 'cfm/',
        'exp_name': watch(diffusion_args_to_watch),

        ## training
        'n_steps_per_epoch': 10000,
        'loss_type': 'l2',
        'n_train_steps': 500000,
        'batch_size': 32,
        'learning_rate': 2e-4,
        'gradient_accumulate_every': 2,
        'ema_decay': 0.995,
        'save_freq': 2000,
        'sample_freq': 2000,
        'n_saves': 50,
        'save_parallel': False,
        'n_reference': 50,
        'n_samples': 10,
        'bucket': None,
        'device': 'cuda',
    },

    'plan': {
        'batch_size': 1,
        'device': 'cuda',

        ## diffusion model
        'horizon': 60,
        'n_diffusion_steps': 100,
        'normalizer': 'LimitsNormalizer',

        ## serialization
        'vis_freq': 10,
        'logbase': 'logs',
        'prefix': 'plans/release',
        'exp_name': watch(plan_args_to_watch),
        'suffix': '0',

        'conditional': False,

        ## loading
        'diffusion_loadpath': 'f:diffusion/H{horizon}_T{n_diffusion_steps}',
        'diffusion_epoch': 'latest',
    },

}