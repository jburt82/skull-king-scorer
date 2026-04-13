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
- **Status**: pending
- **Priority**: high
- **Description**: Back button not properly tracking previous page navigation
- **Details**: Currently goes to hardcoded screens instead of actual previous page

---

<!-- Add your changes above this line -->

## Notes
- Edit this file anytime from your phone or computer
- Commit to GitHub when ready
- Tell me "Check CHANGES.md" in chat and I'll implement them
- I'll update status to "done" when implemented and committed
