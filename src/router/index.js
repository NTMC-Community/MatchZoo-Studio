import Vue from 'vue'
import Router from 'vue-router'
import MatchZooIntroduction from '@/components/MatchZoo/Index/MatchZooIntroduction'
import Introduction1 from '@/components/MatchZoo/Index/Introduction1.md'
import DRMM from '@/components/MatchZoo/DRMM/DRMM'
import DSSM from '@/components/MatchZoo/DSSM/DSSM'
import CDSSM from '@/components/MatchZoo/CDSSM/CDSSM'
import ARCI from '@/components/MatchZoo/ARCI/ARCI'
import ARCII from '@/components/MatchZoo/ARCII/ARCII'
import MatchPyramid from '@/components/MatchZoo/Matchpyramid/Matchpyramid'
import DUET from '@/components/MatchZoo/DUET/DUET'
import MVLSTM from '@/components/MatchZoo/MVLSTM/MVLSTM'
import ANMM from '@/components/MatchZoo/ANMM/ANMM'
import KNRM from '@/components/MatchZoo/KNRM/KNRM'
import CONV_KNRM from '@/components/MatchZoo/CONV_KNRM/CONV_KNRM'
import NewModel from '@/components/MatchZoo/NEW_MODEL/NewModel'
import Tune from '@/components/MatchZoo/Tune/Tune'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MatchZooIntroduction',
      component: MatchZooIntroduction
    },
    {
      path: '/introduction1',
      name: 'Introduction1',
      component: Introduction1
    },
    {
      path: '/drmm',
      name: 'DRMM',
      component: DRMM
    },
    {
      path: '/dssm',
      name: 'DSSM',
      component: DSSM
    },
    {
      path: '/arcii',
      name: 'ARCII',
      component: ARCII
    },
    {
      path: '/arci',
      name: 'ARCI',
      component: ARCI
    },
    {
      path: '/cdssm',
      name: 'CDSSM',
      component: CDSSM
    },
    {
      path: '/matchpyramid',
      name: 'MatchPyramid',
      component: MatchPyramid
    },
    {
      path: '/duet',
      name: 'DUET',
      component: DUET
    },
    {
      path: '/mvlstm',
      name: 'MVLSTM',
      component: MVLSTM
    },
    {
      path: '/anmm',
      name: 'ANMM',
      component: ANMM
    },
    {
      path: '/knrm',
      name: 'KNRM',
      component: KNRM
    },
    {
      path: '/conv_knrm',
      name: 'CONV_KNRM',
      component: CONV_KNRM
    },
    {
      path: '/new_model',
      name: 'NewModel',
      component: NewModel
    },
    {
      path: '/tune',
      name: 'Tune',
      component: Tune
    }
  ]
})
