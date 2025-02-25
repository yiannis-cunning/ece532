




module knn_block(
    input clk,
    input resetn,

    // SRAM data input - starts at address 0x0 - where the input image is stored
    output wire [31:0] img_addr,
    input wire [31:0] img_rdata


    // SRAM weight block - for any weight data that needs to be read
    output wire [31:0] w_addr,
    input wire [31:0] w_rdata


    // Control and status signals
    input wire start_inference,
    output wire done_inference,
    output wire [2:0] infered_digit
);





endmodule