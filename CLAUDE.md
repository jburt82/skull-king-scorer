# Skull King Scorer App — Architecture Guide

## Overview
A mobile-first Progressive Web App (PWA) for scoring the Skull King card game. Single-file HTML application with embedded CSS and JavaScript.

## App Structure

### Game Screens
- **Setup (s-setup)**: Add players, choose game mode, set number of rounds
- **Bid (s-bid)**: Players enter their bids for tricks they'll win
- **Score (s-score)**: Record actual tricks won and any bonuses earned
- **Board (s-board)**: View standings after each round
- **Final (s-final)**: Winner announcement and final standings
- **Edit (s-edit)**: Modify scores from any past round

### Game Modes
- **Classic**: Hit exact bid = 20pts × tricks. Miss = −10pts × tricks off. Zero bid = ±10pts per round
- **Rascal**: Hit exact bid = 10pts per round. Off by 1 = half points. Off by 2+ = 0pts. Zero bid = ±10pts per round

### Bonuses (Only count when bid is hit)
- 💀 Skull King captured by Mermaid: 40 pts (max 1)
- ⚓ Pirate captured by Skull King: 30 pts each (max 5)
- 🧜 Mermaid captured by Pirate: 20 pts each (max 2)
- 🏴 Black 14 Flag: 20 pts (max 1)
- 🏳 Colored 14 Flags: 10 pts each (max 3)

## Key Game State (Object G)
```
G = {
  mode: 'classic' or 'rascal',
  rounds: 1-10,
  players: [{name, scores[], bids[], tricks[], bonuses[], bonusData[]}],
  round: current round number,
  bidIdx: current player index,
  tempBids, tempTricks, tempBonuses: temporary storage during round
}
```

## Key Functions by Category

### Screen Navigation
- `show(id)` - Switch to a screen
- `initSetup()` - Initialize setup screen
- `toast(msg)` - Show temporary notification

### Game Flow
- `startGame()` - Begin game with current players
- `showBidScreen()` - Display bid entry for current round
- `submitBids()` - Move from bid screen to score screen
- `showScoreScreen()` - Display score entry
- `calcScores()` - Calculate and save round scores
- `showBoard()` - Display standings
- `nextRound()` - Move to next round
- `showFinal()` - Display game complete screen

### Players & Setup
- `addPlayer()` - Add a new player
- `rmPlayer(idx)` - Remove player at index
- `renderPlist()` - Render player list
- `saveCurrentNames()` - Save player names to localStorage
- `getSaved()` / `setSaved()` - Get/set saved player list

### Bid & Score Input
- `renderBidCards()` - Render bid input for all players
- `chBid(idx, d)` - Change bid value
- `renderAllScoreRows()` - Render score entry panels
- `chTricks(idx, d)` - Change tricks value
- `chBonus(idx, key, d, max)` - Change bonus value

### Scoring Logic
- `calcScore(bid, tricks, bonus, round, mode)` - Calculate single player score
- `totalBonus(idx)` - Sum all bonuses for a player
- `buildStandingsTable(id, numRounds)` - Generate standings table HTML
- `total(p)` - Calculate total score for a player

### Editing Past Rounds
- `openEditRound(r, from)` - Open edit mode for round r
- `saveEditRound()` - Save edits and return to previous screen
- `cancelEdit()` - Discard edits

### UI Components
- `openBonusSheet(idx)` - Open bonus input bottom sheet
- `closeBonusSheet()` - Close bonus sheet
- `updateSheetPreview(idx)` - Update bonus preview

## Data Persistence
- Player names saved to `localStorage['skullKingSaved']` as JSON array
- All game data stored in memory during play (not persisted to localStorage)

## Styling System
Uses CSS variables for theming:
- Colors: `--navy`, `--gold`, `--gold-bright`, `--text`, `--success`, `--danger`
- Spacing: Standard 8px grid
- Border radius: `--r: 13px`
- Typography: Cinzel (headings), Crimson Text (body)

## Features
- 2-6 player support
- 1-10 rounds per game
- Save/load player names
- Edit any past round
- Responsive mobile design
- PWA capable (manifest.json + sw.js)
- Touch-optimized UI

## Files in Repo
- `index.html` - Main app (all code)
- `manifest.json` - PWA manifest
- `sw.js` - Service worker for offline support
- `CLAUDE.md` - This file
- `CHANGES.md` - Your change requests (edit on phone/desktop)
