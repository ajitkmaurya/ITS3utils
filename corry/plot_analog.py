#!/bin/env python3

import sys, os, json,argparse

parser = argparse.ArgumentParser(description='Post-processing script for corryvreckan')
parser.add_argument('-f', '--file',help='Output histogram from corry', default="analog-debug.root")
parser.add_argument('-o', '--output',help='Output file path', default='cluster.root')
parser.add_argument('-p', '--print',help='Print in PDF file', default='cluster.pdf')

args = parser.parse_args()

import ROOT
from plot_util import *

args.print = args.output.replace('.root','.pdf')

ALICEStyle()
ROOT.gStyle.SetOptTitle(1)
ROOT.gStyle.SetOptStat(1)
global c
c = ROOT.TCanvas('cQA','Corry Performance Figures',2560, 1440)
c.SetMargin(0.15, 0.02, 0.15, 0.1)
c.Draw()

# Sub-pads
subPadNX = 4
subPadNY = 3
global padIndex
padIndex = 0

#TODO: create class Painter to integrate function and vars
def NextPad(title=""):
  global padIndex
  if(padIndex == subPadNX * subPadNY):
    c.Print(args.print, "Title:"+title)
    c.Clear()
    c.Divide(subPadNX, subPadNY)
    padIndex = 1
  else:
    padIndex = padIndex + 1
  c.cd(padIndex)
# Draw and print canvas
def DrawHist(htmp, title="", option="", optStat=True, samePad=False):
  ROOT.gStyle.SetOptStat(optStat)
  if(title == ""):
    title = htmp.GetTitle()
  if(not samePad):
    NextPad(title)
  print("[+] DEBUG - Pad " + str(padIndex) + ' : ' + htmp.GetName()) 
  htmp.Draw(option)

PrintCover(c, args.print)

c.Divide(subPadNX, subPadNY) # Divide again after canvas.Clear

corryHist = ROOT.TFile(args.file)

clusterModule = "ClusteringAnalog"
analysisModule = "AnalysisDUT"
detector = "CE65_4"

dirCluster = corryHist.Get(clusterModule).Get(detector)
dirAna = corryHist.Get(analysisModule).Get(detector)

hMap = dirCluster.Get("clusterPositionLocal")
DrawHist(hMap, "Cluster neighbours charge","colz")

hSize = dirCluster.Get("clusterSize")
hSize.GetXaxis().SetRangeUser(0,30)
DrawHist(hSize, "clusterSize")

hSize = dirCluster.Get("clusterCharge")
hSize.Rebin(int(100. / hSize.GetBinWidth(1)))
hSize.GetXaxis().SetRangeUser(-5000,20000)
DrawHist(hSize, "clusterSize")


hSize = dirCluster.Get("clusterSeedCharge")
hSize.Rebin(int(100. / hSize.GetBinWidth(1)))
hSize.GetXaxis().SetRangeUser(0,12000)
DrawHist(hSize, "clusterSize")

hSize = dirCluster.Get("clusterNeighboursCharge")
hSize.Rebin(int(100. / hSize.GetBinWidth(1)))
hSize.GetXaxis().SetRangeUser(-5000,5000)
DrawHist(hSize, "clusterSize")

hSize = dirCluster.Get("clusterNeighboursChargeSum")
hSize.Rebin(int(100. / hSize.GetBinWidth(1)))
hSize.GetXaxis().SetRangeUser(-5000,10000)
DrawHist(hSize, "Cluster neighbours charge")

hRatio = dirCluster.Get("clusterChargeRatio")
hRatio.GetXaxis().SetRangeUser(0,10)
hRatio.GetYaxis().SetRangeUser(0,1.1)
DrawHist(hRatio, "Cluster charge ratio", "colz", False)

hSize = dirCluster.Get("clusterSeedSNR")
hSize.Rebin(int(0.5 / hSize.GetBinWidth(1)))
hSize.GetXaxis().SetRangeUser(0,100)
DrawHist(hSize, "clusterSeedSNR")

hSize = dirCluster.Get("clusterNeighboursSNR")
hSize.GetXaxis().SetRangeUser(-10,10)
DrawHist(hSize, "clusterNeighboursSNR")

hMap = dirCluster.Get("clusterSeed_Neighbours")
hMap.GetYaxis().SetRangeUser(-4000,10000)
DrawHist(hMap, "clusterSeed_Neighbours", "colz", False)

hMap = dirCluster.Get("clusterSeed_NeighboursSNR")
DrawHist(hMap, "clusterSeed_NeighboursSNR", "colz", False)

hMap = dirCluster.Get("clusterSeed_NeighboursSum")
hMap.GetYaxis().SetRangeUser(-4000,10000)
DrawHist(hMap, "clusterSeed_NeighboursSum", "colz", False)

hMap = dirCluster.Get("clusterSeed_Cluster")
hMap.GetYaxis().SetRangeUser(-4000,10000)
DrawHist(hMap, "clusterSeed_Cluster", "colz", False)

hMap = dirCluster.Get("clusterSeedSNR_Cluster")
DrawHist(hMap, "clusterSeedSNR_Cluster", "colz", False)

hMap = dirCluster.Get("clusterChargeShape")
hMap.GetXaxis().SetRangeUser(-5,5)
DrawHist(hMap, "clusterChargeShape", "colz", False)

hMap = dirCluster.Get("clusterChargeShapeSNR")
hMap.GetXaxis().SetRangeUser(-5,5)
DrawHist(hMap, "clusterChargeShapeSNR", "colz", False)

hMap = dirCluster.Get("clusterChargeShapeRatio")
hMap.GetXaxis().SetRangeUser(-5,5)
DrawHist(hMap, "clusterChargeShapeRatio", "colz", False)

hMap = dirAna.Get("clusterMapAssoc")
DrawHist(hMap, "clusterSize", "colz")

hSigX = dirAna.Get("global_residuals").Get("residualsX")
hSigX.Rebin(int(1. / hSigX.GetBinWidth(1)))
NextPad()
hSigX.Fit("gaus","","",-50,50)
hSigX.GetXaxis().SetRangeUser(-50,50)
DrawHist(hSigX, "clusterSize", samePad=True)

hSigX = dirAna.Get("global_residuals").Get("residualsY")
hSigX.Rebin(int(1. / hSigX.GetBinWidth(1)))
NextPad()
hSigX.Fit("gaus","","",-50,50)
hSigX.GetXaxis().SetRangeUser(-50,50)
DrawHist(hSigX, "clusterSize", samePad=True)

c.Print(args.print, "Title:last")

PrintCover(c, args.print, isBack=True)
corryHist.Close()