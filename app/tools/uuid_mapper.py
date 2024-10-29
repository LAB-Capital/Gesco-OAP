def text_to_uuid(target_df, donor_df, entidad_col, uuid_col):
    donor_df.drop(columns=['sector'],inplace=True)
    merged_df = target_df.merge(donor_df, on=entidad_col, how='left')
    merged_df[entidad_col] = merged_df[uuid_col].combine_first(merged_df[entidad_col])
    merged_df = merged_df.drop(columns=[uuid_col])

    return merged_df
    
def uuid_to_text(target_df, donor_df, entidad_col, uuid_col):
    donor_df.drop(columns=['sector'],inplace=True)
    merged_df = target_df.merge(donor_df, on=uuid_col, how='left')
    merged_df[uuid_col] = merged_df[entidad_col].combine_first(merged_df[uuid_col])
    merged_df = merged_df.drop(columns=[entidad_col])

    return merged_df
