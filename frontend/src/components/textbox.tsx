import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";

export default function Textbox() {
  const charLimit = 100;

  return (
    <div>
      <Box
        component="form"
        sx={{
          "& .MuiTextField-root": { m: 1, width: "25ch" },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField
          id="outlined-multiline-static"
          label="Multiline"
          multiline
          rows={4}
          defaultValue="Default Value"
        />
      </Box>
    </div>
  );
}
