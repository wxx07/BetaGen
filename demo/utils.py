# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:27:05 2020

@author: olive
"""

import py3Dmol

def show_lig_betas(lig_betas_sdf):

    all_sdf = open(lig_betas_sdf,"r").readlines()
    all_sdf = "".join(list(all_sdf))

    view = py3Dmol.view()
    view.addModels(all_sdf,'sdf') 
    view.setStyle({"model":0},{"sphere":{"radius":0.5,"color":"0x33FF38"}}) 
    view.setStyle({"model":1},{"stick":{}})

    view.zoomTo()
    return view


def show_gen_step(step_i):
    all_sdf = open(f"./one_beta/step_{step_i}.sdf","r").readlines()
    all_sdf = "".join(list(all_sdf))

    view = py3Dmol.view()
    view.addModels(all_sdf,'sdf') # 必须用addModels导入储存多个分子的sdf文件
    view.setStyle({"model":0},{"sphere":{"radius":0.5,"color":"0x33FF38"}}) # 颜色hex number前需要有0x
    view.setStyle({"model":1},{"sphere":{"radius":0.5,"color":"0x33FF38","opacity":0.5}}) # 颜色hex number前需要有0x

    if step_i > 0:
        view.setStyle({"model":2},{"stick":{}})
        view.addStyle({"model":2},{"sphere":{"radius":0.5}})
    else:
        view.setStyle({"model":2},{"sphere":{"radius":0.5}})


    view.zoomTo()
    return view


def show_gen_step2(sdf_root, step_i,
                   opacity=0.5, last_step=False,
                   show_all_atlast=False, show_nnhb_betas=False):
    """contains 3 parts: beta atoms, generated ligand atoms and focused ligand atom
                        (new)may contain non-neighbor beta atoms
    Args
        opacity(float): control opacity of focused ligand atoms
        last_step(bool): whether it is the last snapshot of generation
        show_all_atlast(bool): whether to show all pocket beta atoms in the last snapshot
        show_nnhb_betas(bool): whether to show non-neighbor beta atoms along with others
    
    """
    
    all_sdf = open(f"{sdf_root}/step_{step_i}.sdf","r").readlines()
    all_sdf = "".join(list(all_sdf))

    view = py3Dmol.view()
    view.addModels(all_sdf,'sdf') 

    view.setStyle({"model":0},{"stick":{}})
    view.addStyle({"model":0},{"sphere":{"radius":0.5}})
    
    if not last_step: # no focus or beta atoms in the last step
        view.setStyle({"model":1},{"sphere":{"radius":0.6,"color":"0xF2840F","opacity":opacity}}) 
        view.setStyle({"model":2},{"sphere":{"radius":0.5,"color":"0x33FF38"}})
        if show_nnhb_betas:
            view.setStyle({"model":3},{"sphere":{"radius":0.5,"color":"0x33FF38","opacity":0.5}}) 
    elif show_all_atlast:
        # show all beta atoms as opaque spheres
        view.setStyle({"model":1},{"sphere":{"radius":0.5,"color":"0x33FF38","opacity":0.5}})

    view.zoomTo()
    return view
