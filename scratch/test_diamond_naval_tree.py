# Generator for 25-focus Diamond Tree (Organic Diamond Flow) for Vietnam Navy

focuses = [
    # LAYER 1: ROOT (Y=2, X=212)
    {
        "id": "VIE_nav_maritime_strategy_21st",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "x": 10,
        "y": 1,
        "relative_position_id": "VIE_modernize_vpa",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_modernize_vpa"}],
        "reward": """			add_political_power = 75
			navy_experience = 25
			add_ideas = VPA_Naval_Readiness_1
			custom_effect_tooltip = VIE_nav_maritime_strategy_21st_tt"""
    },

    # LAYER 2: DUAL BRIDGES (Y=3, X=207 & 217)
    {
        "id": "VIE_nav_russian_naval_partnership",
        "icon": "GFX_focus_VIE_naval_mro",
        "x": -5,
        "y": 1,
        "relative_position_id": "VIE_nav_maritime_strategy_21st",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_maritime_strategy_21st"}],
        "reward": """			navy_experience = 30
			add_opinion_modifier = { target = RUS modifier = VIE_naval_technical_cooperation }
			custom_effect_tooltip = VIE_nav_russian_naval_partnership_tt"""
    },
    {
        "id": "VIE_nav_bason_shipbuilding_core",
        "icon": "GFX_focus_VIE_ba_son_shipyards",
        "x": 5,
        "y": 1,
        "relative_position_id": "VIE_nav_maritime_strategy_21st",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_maritime_strategy_21st"}],
        "reward": """			add_ideas = VIE_naval_shipbuilding_spirit
			520 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = dockyard
					level = 1
					instant_build = yes
				}
			}
			custom_effect_tooltip = VIE_nav_bason_shipbuilding_core_tt"""
    },

    # LAYER 3: FOUR CAPABILITY ANCHORS (Y=4, X=205, 209, 215, 219)
    {
        "id": "VIE_nav_kilo_submarine_procurement",
        "icon": "GFX_focus_VIE_nf_submarine_force",
        "x": -2,
        "y": 1,
        "relative_position_id": "VIE_nav_russian_naval_partnership",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_russian_naval_partnership"}],
        "reward": """			navy_experience = 30
			set_temp_variable = { treasury_change = -3 }
			modify_treasury_effect = yes
			add_tech_bonus = {
				name = VIE_sub_tech_bonus
				bonus = 0.50
				uses = 2
				category = ss_tech
			}
			custom_effect_tooltip = VIE_nav_kilo_submarine_procurement_tt"""
    },
    {
        "id": "VIE_nav_gepard_frigate_procurement",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "x": 2,
        "y": 1,
        "relative_position_id": "VIE_nav_russian_naval_partnership",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_russian_naval_partnership"}],
        "reward": """			navy_experience = 30
			set_temp_variable = { treasury_change = -3 }
			modify_treasury_effect = yes
			add_tech_bonus = {
				name = VIE_frigate_tech_bonus
				bonus = 0.50
				uses = 2
				category = dd_tech
			}
			custom_effect_tooltip = VIE_nav_gepard_frigate_procurement_tt"""
    },
    {
        "id": "VIE_nav_molniya_fast_attack_craft",
        "icon": "GFX_focus_VIE_nf_first_force",
        "x": -2,
        "y": 1,
        "relative_position_id": "VIE_nav_bason_shipbuilding_core",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_bason_shipbuilding_core"},
            {"focus": "VIE_nav_russian_naval_partnership"}
        ],
        "reward": """			navy_experience = 25
			swap_ideas = {
				remove_idea = VIE_naval_shipbuilding_spirit
				add_idea = VIE_naval_shipbuilding_spirit_2
			}
			custom_effect_tooltip = VIE_nav_molniya_fast_attack_craft_tt"""
    },
    {
        "id": "VIE_nav_cam_ranh_naval_base",
        "icon": "GFX_focus_VIE_scs_cam_ranh_port",
        "x": 2,
        "y": 1,
        "relative_position_id": "VIE_nav_bason_shipbuilding_core",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_bason_shipbuilding_core"}],
        "reward": """			522 = {
				add_building_construction = {
					type = naval_base
					level = 2
					instant_build = yes
					province = 7288
				}
			}
			add_ideas = VIE_fleet_sustainment_spirit
			custom_effect_tooltip = VIE_nav_cam_ranh_naval_base_tt"""
    },

    # LAYER 4: EIGHT EXPEDITIONARY & WEAPONS SYSTEMS (Y=5, X=205, 207, 209, 211, 213, 215, 217, 219)
    {
        "id": "VIE_nav_189th_submarine_brigade",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_kilo_submarine_procurement",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_kilo_submarine_procurement"}],
        "reward": """			navy_experience = 25
			add_ideas = VIE_189th_submarine_brigade_spirit
			custom_effect_tooltip = VIE_nav_189th_submarine_brigade_tt"""
    },
    {
        "id": "VIE_nav_clubs_cruise_missiles",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "x": 2,
        "y": 1,
        "relative_position_id": "VIE_nav_kilo_submarine_procurement",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_kilo_submarine_procurement"}],
        "reward": """			navy_experience = 25
			add_tech_bonus = {
				name = VIE_missile_tech_bonus
				bonus = 0.50
				uses = 1
				category = rocketry
			}
			custom_effect_tooltip = VIE_nav_clubs_cruise_missiles_tt"""
    },
    {
        "id": "VIE_nav_162nd_frigate_brigade",
        "icon": "GFX_focus_VIE_nf_surface_force",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_gepard_frigate_procurement",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_gepard_frigate_procurement"}],
        "reward": """			navy_experience = 25
			add_ideas = VIE_162nd_frigate_brigade_spirit
			custom_effect_tooltip = VIE_nav_162nd_frigate_brigade_tt"""
    },
    {
        "id": "VIE_nav_naval_aviation_ka28",
        "icon": "GFX_focus_VIE_nf_naval_aviation",
        "x": 2,
        "y": 1,
        "relative_position_id": "VIE_nav_gepard_frigate_procurement",
        "cost": 5,
        "prerequisite": [{"focus": "VIE_nav_gepard_frigate_procurement"}],
        "reward": """			air_experience = 20
			navy_experience = 15
			add_tech_bonus = {
				name = VIE_naval_air_tech_bonus
				bonus = 0.50
				uses = 1
				category = cat_naval_air
			}
			custom_effect_tooltip = VIE_nav_naval_aviation_ka28_tt"""
    },
    {
        "id": "VIE_nav_uran_e_integration",
        "icon": "GFX_focus_VIE_naval_systems_integration",
        "x": -2,
        "y": 1,
        "relative_position_id": "VIE_nav_molniya_fast_attack_craft",
        "cost": 5,
        "prerequisite": [{"focus": "VIE_nav_molniya_fast_attack_craft"}],
        "reward": """			navy_experience = 20
			add_ideas = VIE_naval_weapons_integration_spirit
			custom_effect_tooltip = VIE_nav_uran_e_integration_tt"""
    },
    {
        "id": "VIE_nav_domestic_patrol_craft",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_molniya_fast_attack_craft",
        "cost": 5,
        "prerequisite": [{"focus": "VIE_nav_molniya_fast_attack_craft"}],
        "reward": """			522 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = dockyard
					level = 1
					instant_build = yes
				}
			}
			custom_effect_tooltip = VIE_nav_domestic_patrol_craft_tt"""
    },
    {
        "id": "VIE_nav_submarine_rescue_logistics",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "x": -2,
        "y": 1,
        "relative_position_id": "VIE_nav_cam_ranh_naval_base",
        "cost": 5,
        "prerequisite": [{"focus": "VIE_nav_cam_ranh_naval_base"}],
        "reward": """			swap_ideas = {
				remove_idea = VIE_fleet_sustainment_spirit
				add_idea = VIE_fleet_sustainment_spirit_2
			}
			custom_effect_tooltip = VIE_nav_submarine_rescue_logistics_tt"""
    },
    {
        "id": "VIE_nav_spratly_dk1_defense_system",
        "icon": "GFX_focus_VIE_scs_spratly_fortification",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_cam_ranh_naval_base",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_cam_ranh_naval_base"}],
        "reward": """			524 = {
				add_building_construction = {
					type = coastal_bunker
					level = 2
					instant_build = yes
					province = 13247
				}
			}
			add_ideas = VIE_island_fortress_spirit
			custom_effect_tooltip = VIE_nav_spratly_dk1_defense_system_tt"""
    },

    # LAYER 5: THREE COMBINED CAPABILITY NODES (Y=6, X=207, 212, 217)
    {
        "id": "VIE_nav_integrated_undersea_warfare",
        "icon": "GFX_focus_VIE_nf_denial",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_clubs_cruise_missiles",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_189th_submarine_brigade"},
            {"focus": "VIE_nav_clubs_cruise_missiles"}
        ],
        "reward": """			navy_experience = 35
			add_ideas = VIE_undersea_warfare_network_spirit
			custom_effect_tooltip = VIE_nav_integrated_undersea_warfare_tt"""
    },
    {
        "id": "VIE_nav_bastion_a2ad_coastal_shield",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "x": 1,
        "y": 1,
        "relative_position_id": "VIE_nav_naval_aviation_ka28",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_162nd_frigate_brigade"},
            {"focus": "VIE_nav_uran_e_integration"}
        ],
        "reward": """			navy_experience = 35
			add_ideas = VIE_coastal_a2ad_shield_spirit
			custom_effect_tooltip = VIE_nav_bastion_a2ad_coastal_shield_tt"""
    },
    {
        "id": "VIE_nav_offshore_task_groups",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_submarine_rescue_logistics",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_domestic_patrol_craft"},
            {"focus": "VIE_nav_submarine_rescue_logistics"},
            {"focus": "VIE_nav_spratly_dk1_defense_system"}
        ],
        "reward": """			navy_experience = 35
			swap_ideas = {
				remove_idea = VPA_Naval_Readiness_1
				add_idea = VPA_Naval_Readiness_2
			}
			custom_effect_tooltip = VIE_nav_offshore_task_groups_tt"""
    },

    # LAYER 6: TWO OPERATIONAL PILLARS (Y=7, X=211 & 213)
    {
        "id": "VIE_nav_c4isr_maritime_domain_awareness",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "x": 4,
        "y": 1,
        "relative_position_id": "VIE_nav_integrated_undersea_warfare",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_integrated_undersea_warfare"},
            {"focus": "VIE_nav_bastion_a2ad_coastal_shield"}
        ],
        "reward": """			navy_experience = 30
			add_ideas = VIE_maritime_domain_awareness_spirit_2
			custom_effect_tooltip = VIE_nav_c4isr_maritime_domain_awareness_tt"""
    },
    {
        "id": "VIE_nav_naval_infantry_and_sappers",
        "icon": "GFX_focus_VIE_sf_marine",
        "x": 1,
        "y": 1,
        "relative_position_id": "VIE_nav_bastion_a2ad_coastal_shield",
        "cost": 7,
        "prerequisite": [
            {"focus": "VIE_nav_bastion_a2ad_coastal_shield"},
            {"focus": "VIE_nav_offshore_task_groups"}
        ],
        "reward": """			army_experience = 25
			navy_experience = 25
			add_ideas = VIE_marine_infantry_readiness_spirit
			custom_effect_tooltip = VIE_nav_naval_infantry_and_sappers_tt"""
    },

    # LAYER 7: PRE-DOCTRINE ADVANCED PREPARATION (Y=8, X=211 & 213)
    {
        "id": "VIE_nav_subsurface_steel_wall",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_c4isr_maritime_domain_awareness",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_c4isr_maritime_domain_awareness"}],
        "reward": """			navy_experience = 35
			add_ideas = VIE_subsurface_steel_wall_spirit
			custom_effect_tooltip = VIE_nav_subsurface_steel_wall_tt"""
    },
    {
        "id": "VIE_nav_integrated_island_fleet_defense",
        "icon": "GFX_focus_VIE_scs_dk1_platforms",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_naval_infantry_and_sappers",
        "cost": 7,
        "prerequisite": [{"focus": "VIE_nav_naval_infantry_and_sappers"}],
        "reward": """			navy_experience = 35
			add_ideas = VIE_island_fleet_defense_spirit
			custom_effect_tooltip = VIE_nav_integrated_island_fleet_defense_tt"""
    },

    # LAYER 8: TWO MUTUALLY EXCLUSIVE DOCTRINE ARCHETYPES (Y=9, X=211 & 213)
    {
        "id": "VIE_nav_doctrine_asymmetric_sea_denial",
        "icon": "GFX_focus_VIE_nf_medium_force",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_subsurface_steel_wall",
        "cost": 10,
        "prerequisite": [{"focus": "VIE_nav_subsurface_steel_wall"}],
        "mutually_exclusive": [{"focus": "VIE_nav_doctrine_active_maritime_presence"}],
        "reward": """			navy_experience = 50
			add_ideas = VIE_doctrine_asymmetric_sea_denial_spirit
			custom_effect_tooltip = VIE_nav_doctrine_asymmetric_sea_denial_tt"""
    },
    {
        "id": "VIE_nav_doctrine_active_maritime_presence",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "x": 0,
        "y": 1,
        "relative_position_id": "VIE_nav_integrated_island_fleet_defense",
        "cost": 10,
        "prerequisite": [{"focus": "VIE_nav_integrated_island_fleet_defense"}],
        "mutually_exclusive": [{"focus": "VIE_nav_doctrine_asymmetric_sea_denial"}],
        "reward": """			navy_experience = 50
			add_ideas = VIE_doctrine_active_maritime_presence_spirit
			custom_effect_tooltip = VIE_nav_doctrine_active_maritime_presence_tt"""
    },

    # LAYER 9: CONVERGING DIAMOND CAPSTONE (Y=10, X=212)
    {
        "id": "VIE_nav_capstone_eastern_sea_sovereignty",
        "icon": "GFX_focus_VIE_naval_defence_law",
        "x": 1,
        "y": 1,
        "relative_position_id": "VIE_nav_doctrine_asymmetric_sea_denial",
        "cost": 10,
        "prerequisite": [
            {"focus": "VIE_nav_doctrine_asymmetric_sea_denial"},
            {"focus": "VIE_nav_doctrine_active_maritime_presence"}
        ],
        "reward": """			add_political_power = 150
			navy_experience = 50
			swap_ideas = {
				remove_idea = VPA_Naval_Readiness_2
				add_idea = VPA_Naval_Readiness_3
			}
			add_ideas = VIE_eastern_sea_sovereignty_capstone_spirit
			custom_effect_tooltip = VIE_nav_capstone_eastern_sea_sovereignty_tt"""
    }
]

print(f"Total diamond focuses: {len(focuses)}")
