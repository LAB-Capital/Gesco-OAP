def autocomputar_2019(df):

    df['i1'] = df['p1']
    df['i2'] = df['p2']
    df['i3'] = df['p3'] + df['p4']
    df['i4'] = df['p5'] + df['p6']
    df['i5'] = df['p7'] + df['p8'] + df['p9']
    df['i6'] = df['p10'] + df['p11'] + df['p12']
    df['i7'] = df['p13']
    df['i8'] = df['p14']
    df['i9'] = df['p15']
    df['i10'] = df['p16']
    df['i11'] = df['p17'] + df['p18']
    df['i12'] = df['p19']
    df['i13'] = df['p20']
    df['i14'] = df['p21'] + df['p22']
    df['i15'] = df['p23']
    df['i16'] = df['p24']
    df['i17'] = df['p25']
    df['i18'] = df['p26']
    df['i19'] = df['p27']
    df['i20'] = df['p28']
    df['i21'] = df['p29']
    df['i22'] = df['p30']
    df['i23'] = df['p31']
    df['i24'] = df['p32']
    df['i25'] = df['p33']
    df['i26'] = df['p34']
    df['i27'] = df['p35']
    df['i28'] = df['p36']
    df['i29'] = df['p37']
    df['i30'] = df['p38']
    df['i31'] = df['p39']

    df['v1'] = df['i1'] + df['i2']
    df['v2'] = df['i3'] + df['i4']
    df['v3'] = df['i5'] + df['i6']
    df['v4'] = df['i7']
    df['v5'] = df['i8'] + df['i9'] + df['i10'] + df['i11']
    df['v6'] = df['i12'] + df['i13'] + df['i14']
    df['v7'] = df['i15']
    df['v8'] = df['i16']
    df['v9'] = df['i17'] + df['i18'] + df['i19']
    df['v10'] = df['i20']
    df['v11'] = df['i21'] + df['i22']
    df['v12'] = df['i23'] + df['i24']
    df['v13'] = df['i25'] + df['i25'] + df['i26'] + df['i27'] + df['i28'] + df['i29'] + df['i30']
    df['v14'] = df['i31']

    df['c1_raw'] = df['v1'] + df['v2'] + df['v3'] + df['v4']
    df['c2_raw'] = df['v5'] + df['v6'] + df['v7'] + df['v8'] + df['v9']
    df['c3_raw'] = df['v10'] + df['v11']
    df['c4_raw'] = df['v12'] + df['v13'] + df['v14']

    df['c1'] = df['c1_raw']*100/25
    df['c2'] = df['c2_raw']*100/35
    df['c3'] = df['c3_raw']*100/25
    df['c4'] = df['c4_raw']*100/15

    df['res'] = df['c1_raw'] + df['c2_raw'] + df['c3_raw'] + df['c4_raw']
    df['res'] = df['res'].fillna(-float('inf'))
    df['pos'] = df['res'].rank(ascending=False, method='min').astype(int)

    return df

def autocomputar_2021(df):
    df['i1'] = df['p1']
    df['i2'] = df['p2']
    df['i3'] = df['p3'] + df['p4']
    df['i4'] = df['p5'] + df['p6']
    df['i5'] = df['p7'] + df['p8'] + df['p9']
    df['i6'] = df['p10'] + df['p11'] + df['p12']
    df['i7'] = df['p13']
    df['i8'] = df['p14']
    df['i9'] = df['p15']
    df['i10'] = df['p16']
    df['i11'] = df['p17'] + df['p18']
    df['i12'] = df['p19']
    df['i13'] = df['p20']
    df['i14'] = df['p21'] + df['p22']
    df['i15'] = df['p23']
    df['i16'] = df['p24']
    df['i17'] = df['p25']
    df['i18'] = df['p26']
    df['i19'] = df['p27']
    df['i20'] = df['p28']
    df['i21'] = df['p29']
    df['i22'] = df['p30']
    df['i23'] = df['p31']
    df['i24'] = df['p32']
    df['i25'] = df['p33']
    df['i26'] = df['p34']
    df['i27'] = df['p35']
    df['i28'] = df['p36']
    df['i29'] = df['p37']
    df['i30'] = df['p38']
    df['i31'] = df['p39']

    df['v1'] = df['i1'] + df['i2']
    df['v2'] = df['i3'] + df['i4']
    df['v3'] = df['i5'] + df['i6']
    df['v4'] = df['i7']
    df['v5'] = df['i8'] + df['i9'] + df['i10'] + df['i11']
    df['v6'] = df['i12'] + df['i13'] + df['i14']
    df['v7'] = df['i15']
    df['v8'] = df['i16']
    df['v9'] = df['i17'] + df['i18'] + df['i19']
    df['v10'] = df['i20']
    df['v11'] = df['i21'] + df['i22']
    df['v12'] = df['i23'] + df['i24']
    df['v13'] = df['i25'] + df['i25'] + df['i26'] + df['i27'] + df['i28'] + df['i29'] + df['i30']
    df['v14'] = df['i31']

    df['c1_raw'] = df['v1'] + df['v2'] + df['v3'] + df['v4']
    df['c2_raw'] = df['v5'] + df['v6'] + df['v7'] + df['v8'] + df['v9']
    df['c3_raw'] = df['v10'] + df['v11']
    df['c4_raw'] = df['v12'] + df['v13'] + df['v14']

    df['c1'] = df['c1_raw']*100/25
    df['c2'] = df['c2_raw']*100/35
    df['c3'] = df['c3_raw']*100/25
    df['c4'] = df['c4_raw']*100/15

    df['res'] = df['c1_raw'] + df['c2_raw'] + df['c3_raw'] + df['c4_raw']
    df['res'] = df['res'].fillna(-float('inf'))
    df['pos'] = df['res'].rank(ascending=False, method='min').astype(int)

    return df

def autocomputar_2023(df):
    df['i1'] = df['p1']
    df['i2'] = df['p2']
    df['i3'] = df['p3'] + df['p4']
    df['i4'] = df['p5'] + df['p6']
    df['i5'] = df['p7'] + df['p8'] + df['p9']
    df['i6'] = df['p10'] + df['p11'] + df['p12']
    df['i7'] = df['p13']
    df['i8'] = df['p14']
    df['i9'] = df['p15']
    df['i10'] = df['p16']
    df['i11'] = df['p17'] + df['p18']
    df['i12'] = df['p19']
    df['i13'] = df['p20']
    df['i14'] = df['p21'] + df['p22']
    df['i15'] = df['p23']
    df['i16'] = df['p24']
    df['i17'] = df['p25']
    df['i18'] = df['p26']
    df['i19'] = df['p27']
    df['i20'] = df['p28']
    df['i21'] = df['p29']
    df['i22'] = df['p30']
    df['i23'] = df['p31']
    df['i24'] = df['p32']
    df['i25'] = df['p33']
    df['i26'] = df['p34']
    df['i27'] = df['p35']
    df['i28'] = df['p36']
    df['i29'] = df['p37']
    df['i30'] = df['p38']
    df['i31'] = df['p39']

    df['v1'] = df['i1'] + df['i2']
    df['v2'] = df['i3'] + df['i4']
    df['v3'] = df['i5'] + df['i6']
    df['v4'] = df['i7']
    df['v5'] = df['i8'] + df['i9'] + df['i10'] + df['i11']
    df['v6'] = df['i12'] + df['i13'] + df['i14']
    df['v7'] = df['i15']
    df['v8'] = df['i16']
    df['v9'] = df['i17'] + df['i18'] + df['i19']
    df['v10'] = df['i20']
    df['v11'] = df['i21'] + df['i22']
    df['v12'] = df['i23'] + df['i24']
    df['v13'] = df['i25'] + df['i25'] + df['i26'] + df['i27'] + df['i28'] + df['i29'] + df['i30']
    df['v14'] = df['i31']

    df['c1_raw'] = df['v1'] + df['v2'] + df['v3'] + df['v4']
    df['c2_raw'] = df['v5'] + df['v6'] + df['v7'] + df['v8'] + df['v9']
    df['c3_raw'] = df['v10'] + df['v11']
    df['c4_raw'] = df['v12'] + df['v13'] + df['v14']

    df['c1'] = df['c1_raw']*100/25
    df['c2'] = df['c2_raw']*100/35
    df['c3'] = df['c3_raw']*100/25
    df['c4'] = df['c4_raw']*100/15

    df['res'] = df['c1_raw'] + df['c2_raw'] + df['c3_raw'] + df['c4_raw']
    df['res'] = df['res'].fillna(-float('inf'))
    df['pos'] = df['res'].rank(ascending=False, method='min').astype(int)

    return df