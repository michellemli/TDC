from ..utils import general_load
from ..utils.load import resource_dataset_load, load_json_from_txt_file 

import pandas as pd

class PINNACLE:
    
    def __init__(self, path="./data"):
        self.ppi_name = "pinnacle_global_ppi_edgelist"
        self.cell_tissue_mg_name = "cell_tissue_mg_edgelist"
        self.ppi = general_load(self.ppi_name, path, " ")
        self.ppi.columns = ["Protein A", "Protein B"]
        self.cell_tissue_mg = general_load(self.cell_tissue_mg_name, path, "\t")  # use tab as names were left with spaces
        self.cell_tissue_mg.columns = ["Tissue", "Cell"]
        self.embeds_name = "pinnacle_protein_embed"
        self.embeds = resource_dataset_load(self.embeds_name, path, [self.embeds_name])
        self.keys = load_json_from_txt_file("pinnacle_labels_dict", path)
    
    def get_ppi(self):
        return self.ppi
    
    def get_mg(self):
        return self.cell_tissue_mg
    
    def get_embeds(self):
        return self.embeds

    def get_keys(self):
        protein_names_celltypes = [p for p in zip(self.keys["Cell Type"], self.keys["Name"]) if not (p[0].startswith("BTO") or p[0].startswith("CCI") or p[0].startswith("Sanity"))]
        proteins = pd.DataFrame.from_dict({"target":[n for _,n in protein_names_celltypes], "cell type":[c for c,_ in protein_names_celltypes]})
        proteins.drop_duplicates()
        return proteins
        
   
   
    
    
    
    