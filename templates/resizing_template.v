


`define RESIZE_WIDTH 23
`define RESIZE_HEIGHT 17


module resizing_block(
    input clk,
    input resetn,

    // AXIS stream input from CPU
    input wire [24:0] m_axis_tdata, // {R[7:0], G[7:0], B[7:0]}
    input wire m_axis_tvalid,
    output wire m_axis_tready


    // Output to SRAM buffer - Starts at address 0x0
    output wire [31:0] addr,
    input wire [31:0] rdata,
    output wire [31:0] wdata,
    output wire wr_en,


    // Control and status signals
    input wire start_bin,           // Command to start the resizing
    output wire bin_done            // Asserted once you have read the whole image
);





endmodule