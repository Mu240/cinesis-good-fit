# Cinesis — Good Fit Test

## Code
https://github.com/Mu240/cinesis-good-fit.git

## Assumptions
- The truck is **currently in Dallas** ("I'm in Dallas") and the driver's **home base is San Antonio** ("based out in San Antonio"). These are different points: deadhead-to-origin starts in Dallas, deadhead-home ends in San Antonio.
- Weight capacity (14,200 lb) is **inferred** — the driver never states it, but he runs a hotshot/gooseneck and the loads he actually books are 11–14k lb, never 38k+.
- All three legs use straight-line **haversine** distance from the provided lat/long.

## How I extracted the profile (Part A)
Parsed the transcript for the driver's own statements rather than the dispatcher's pitch: equipment ("I run a hotshot gooseneck trailer"), minimum rate ("above $2 per mile, I'll consider it"), current location, and home base. Implied fields (home base, capacity) are captured as interpretations with notes.

## Filtering (before ranking)
A load is eligible only if: trailer ∈ {Hotshot, Gooseneck}, weight ≤ 14,200 lb, and effective rate ≥ $2.00/mi.

## Incomplete rows
Rows missing price or destination are **dropped as ineligible** (can't compute a rate) instead of crashing — L06 (no price) and L07 (no destination) excluded.

## High-paying load rejected
**L06** (Shreveport→Atlanta, $—): a 46,500 lb Van — wrong trailer **and** far over capacity, with no listed price. Triple disqualification. Also note L08 pays the most on the board ($1,700) yet ranks #2, because its McAllen destination forces a long empty haul home.

## Top 3 (effective rate/mile)
1. L03 — 3.098
2. L08 — 2.480
3. L02 — 2.418
