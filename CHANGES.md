# Change Requests for Skull King Scorer

Add your requested changes below. I'll check this file before each session and implement them.

## Format
```
### [FEATURE/BUG/ENHANCEMENT] — Brief title
- **Status**: pending / in-progress / done
- **Priority**: high / medium / low
- **Description**: What you want changed
- **Details**: Any additional context or specifications
```

## Your Requests

### Increase max players from 6 to 8
- **Status**: pending
- **Priority**: high
- **Description**: Allow 8 players instead of current max of 6
- **Details**: Update validation and UI to support 2-8 players

### Fix edit previous round functionality
- **Status**: pending
- **Priority**: high
- **Description**: Pencil icon on final score page not opening edit modal
- **Details**: Debug why clicking edit button doesn't open s-edit screen

### Remove icons on final score page
- **Status**: pending
- **Priority**: medium
- **Description**: Remove player icons next to names on final standings table
- **Details**: Keep the player names, just remove the emoji/icon column

### Display row numbers on scoring page
- **Status**: pending
- **Priority**: medium
- **Description**: Add row numbers (1, 2, 3, etc.) to the score entry panels
- **Details**: Number each player's scoring row for clarity during entry

### Save game state for incomplete games
- **Status**: pending
- **Priority**: high
- **Description**: Allow users to save progress and resume a game later
- **Details**: Save to localStorage with date/time. Show option on setup screen to "Resume Game" if one exists. Store: players, current round, bids, tricks, bonuses, scores

### Delete saved games
- **Status**: pending
- **Priority**: high
- **Description**: Add ability to delete previously saved incomplete games
- **Details**: Show delete button next to "Resume Game" option if a saved game exists

### Fix back button history tracking
- **Status**: in-progress
- **Priority**: high
- **Description**: Back button toggles between same two screens instead of going back through history
- **Details**: Round 3 back button goes to round 2, but clicking back again toggles between round 2 and 3 instead of going to round 1

### Fix pencil icon for editing rounds (still broken)
- **Status**: pending
- **Priority**: high
- **Description**: Pencil edit buttons on standings pages not opening edit modal
- **Details**: Clicking edit button should open s-edit screen, but nothing happens

### Games not saving when exited prematurely
- **Status**: pending
- **Priority**: high
- **Description**: No option to resume if user closes game mid-play
- **Details**: Need to trigger save on every screen transition, not just after calcScores

### Make flag icons consistent
- **Status**: pending
- **Priority**: medium
- **Description**: Black flag and colored flag should look the same except color
- **Details**: Black flag = 🏴 (black), Colored flag = green or yellow version. Make them match visually

### Add red shield with crossing swords icon
- **Status**: pending
- **Priority**: medium
- **Description**: Need custom icon for new bonus (looks like pirate/battle icon)
- **Details**: SVG or emoji of red shield with two swords crossing

### Add "Other" bonus type with coins icon
- **Status**: pending
- **Priority**: medium
- **Description**: New bonus category for miscellaneous bonuses
- **Details**: Icon = coins, increments by tens (0-50 or similar max)

### Add row numbers to standings page
- **Status**: pending
- **Priority**: low
- **Description**: Number each row on the standings/board page (1, 2, 3, etc.)
- **Details**: Display on left side like the bid and score pages

### Remove row numbers from bid page
- **Status**: pending
- **Priority**: low
- **Description**: Remove the numbered circles next to player names on bid page
- **Details**: Keep row numbers on score page, just remove from bid page

### Add continue or new game choice
- **Status**: pending
- **Priority**: high
- **Description**: When starting a new game, let user choose to continue old game or start fresh (deletes old)
- **Details**: If saved game exists, show both "Resume" and "New Game" buttons on setup screen

### Confirm pencil icons work on standings page
- **Status**: pending
- **Priority**: high
- **Description**: Verify pencil icons on standings page allow editing previous rounds
- **Details**: Should be able to click any round's pencil icon to edit that round

---

<!-- Add your changes above this line -->

## Notes
- Edit this file anytime from your phone or computer
- Commit to GitHub when ready
- Tell me "Check CHANGES.md" in chat and I'll implement them
- I'll update status to "done" when implemented and committed
