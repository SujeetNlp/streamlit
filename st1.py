import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

iris = pd.read_csv('/Users/sujeet/Downloads/final_file.tsv' ,  sep='\t')

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
	    height=450,
	    width='100%',
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection



okk1 = pd.read_csv('/Users/sujeet/Downloads/send_id.csv')

id_sen_dict  = okk1.set_index('sent_id').to_dict()['sentence']

selection = aggrid_interactive_table(df=iris)

print(selection)
if selection["selected_rows"]:
    key = selection["selected_rows"][0]['sent_id']
    head_index = selection["selected_rows"][0]['head_index']
    row  = iris.loc[(iris['sent_id'] == key)& (iris['index'] == head_index)]
    st.header("Sentence")
    st.write(id_sen_dict[key])
    st.header("Dependent Information")
    st.json(selection["selected_rows"])
    st.header("Head Information")
    st.json(row.to_dict(orient='index'))
    
    