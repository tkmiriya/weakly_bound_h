from src.luscher_lib import Kcot_luscher, Luscher_zeta
import numpy as np


def test_rest_frame_k2_neg():
    L = 24
    m_1 = 0.5
    m_2 = 0.5
    lz = Kcot_luscher(L, m_1, m_2, d=[0,0,0])

    k2 = -1e-2
    val = lz.kcot(k2)
    expect = -0.0571898
    np.testing.assert_almost_equal(val, expect, decimal=5)


def test_rest_frame_k2_pos():
    L = 24
    m_1 = 0.5
    m_2 = 0.5
    lz = Kcot_luscher(L, m_1, m_2, d=[0,0,0])

    k2 = 4e-2
    val = lz.kcot(k2)
    expect = 0.0663662
    np.testing.assert_almost_equal(val, expect, decimal=5)


def test_boosted_frame_k2_neg():
    L = 24
    m_1 = 0.5
    m_2 = 0.5
    lz = Kcot_luscher(L, m_1, m_2, d=[0,0,1])

    k2 = -1e-2
    val = lz.kcot(k2)
    expect = -0.0986194
    np.testing.assert_almost_equal(val, expect, decimal=5)


def test_boosted_frame_k2_pos():
    L = 24
    m_1 = 0.5
    m_2 = 0.5
    lz = Kcot_luscher(L, m_1, m_2, d=[0,0,1])

    k2 = 4e-2
    val = lz.kcot(k2)
    expect = -0.0535232
    np.testing.assert_almost_equal(val, expect, decimal=5)
